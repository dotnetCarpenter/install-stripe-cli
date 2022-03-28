#!/usr/bin/env bash
# -*- coding: utf-8 -*-

beforeAll () {
	local test_dir
	test_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

	source "$test_dir/osht.sh"
	source "$test_dir/../install-stripe-cli"
}

beforeAll

PLAN 1

NRUNS assertChecksumFile






# downloadChecksumFixture () {
# 	downloadChecksums
# 	mv "$STRIPE_LINUX_CHECKSUMS_FILE" fixtures
# }
# downloadChecksumFixture
