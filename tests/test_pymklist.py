#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `pymklist` package."""
import os
import pytest

from click.testing import CliRunner

from pymklist import cli

import mock

from pymklist.download_data import LDRAW_URL


@pytest.fixture
def runner():
    return CliRunner()


@pytest.fixture
def cwd_mock():
    with mock.patch('os.getcwd') as ctx:
        yield ctx


@pytest.fixture
def exists_mock():
    with mock.patch('os.path.exists') as ctx:
        yield ctx


@pytest.fixture
def input_mock():
    with mock.patch('pymklist.cli.six_input') as ctx:
        yield ctx


def test_cli_not_valid_ldraw(cwd_mock, exists_mock, runner):
    cwd_mock.side_effect = lambda: 'invalid_dir'
    exists_mock.side_effect = lambda s: False

    result = runner.invoke(cli.main)
    assert result.exit_code == 1
    assert 'make-list' in result.output


def test_cli_in_valid_ldraw_dir(cwd_mock, exists_mock, runner):
    cwd_mock.side_effect = lambda: 'ldraw'
    exists_mock.side_effect = lambda s: True

    result = runner.invoke(cli.main)
    assert result.exit_code == 0


def test_cli_in_ldraw_dir_without_parts_dir_no(input_mock, cwd_mock, exists_mock, runner):
    cwd_mock.side_effect = lambda: 'ldraw'
    exists_mock.side_effect = lambda s: False
    input_mock.side_effect = lambda t: 'n'

    result = runner.invoke(cli.main)
    assert result.exit_code == 1


def mocked_retrieve(*args, **kwargs):
    return os.path.join('tests','test_data','complete.zip'), ''


@mock.patch('pymklist.download_data.urlretrieve')
@mock.patch('zipfile.ZipFile.extractall')
def test_cli_in_ldraw_dir_without_parts_dir_yes(zip_mock, retrieve_mock, input_mock, cwd_mock, exists_mock, runner):
    cwd_mock.side_effect = lambda: 'ldraw'
    retrieve_mock.side_effect = mocked_retrieve

    def exists(s):
        if s.endswith('.zip'):
            return False
        return False

    exists_mock.side_effect = exists
    input_mock.side_effect = lambda t: 'y'

    result = runner.invoke(cli.main)
    assert result.exit_code == 0

    assert retrieve_mock.called

    assert retrieve_mock.call_args[0][0] == LDRAW_URL

    assert zip_mock.called
    zip_mock.assert_called_with('ldraw')


def test_cli_has_help(runner):
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output
