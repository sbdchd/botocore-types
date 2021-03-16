# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## 0.2.2 - 2020-03-16

### Fixed

- make `botocore.Config.retry` dict `total=False`

## 0.2.1 - 2021-03-16

### Fixed

- added missing `total_max_attempts` and `mode` properties on `Config.retry` dict
