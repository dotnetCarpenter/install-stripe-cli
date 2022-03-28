#!/usr/bin/env bash
# -*- coding: utf-8 -*-

source ../install-stripe-cli







downloadChecksumFixture () {
	downloadChecksums
	mv "$STRIPE_LINUX_CHECKSUMS_FILE" fixtures
}

