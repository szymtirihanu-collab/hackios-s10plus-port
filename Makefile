PYTHON ?= python3

.PHONY: help preflight prepare toolchain validate test clean

help:
	@echo "Targets:"
	@echo "  preflight  Check host tools and target config"
	@echo "  prepare    Create ignored build directories (host-only)"
	@echo "  toolchain Probe installed host tools (read-only)"
	@echo "  validate   Validate generated artifact manifest"
	@echo "  test       Run repository host tests"
	@echo "  clean      Remove ignored build output only"

preflight:
	$(PYTHON) scripts/preflight.py

prepare:
	$(PYTHON) scripts/prepare_build.py

toolchain:
	$(PYTHON) scripts/toolchain_probe.py

validate:
	$(PYTHON) scripts/validate_artifacts.py

test:
	$(PYTHON) -m unittest discover -s tests -v

clean:
	rm -rf build/
