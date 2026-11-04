#!/usr/bin/env bash
# Read-only sanity checks for a previously cloned Exynos 9820 kernel tree.
# Usage: ./scripts/check-kernel-tree.sh /path/to/kernel-source
set -euo pipefail

if [ "$#" -ne 1 ]; then
  echo "Usage: $0 /path/to/kernel-source" >&2
  exit 2
fi

tree=$(cd "$1" && pwd)
echo "Kernel tree: $tree"

for item in Makefile Kconfig arch/arm64; do
  if [ -e "$tree/$item" ]; then
    printf 'OK      %s\n' "$item"
  else
    printf 'MISSING %s\n' "$item"
  fi
done

if [ -f "$tree/Makefile" ]; then
  echo
  echo "Kernel version fields:"
  grep -E '^(VERSION|PATCHLEVEL|SUBLEVEL|EXTRAVERSION)[[:space:]]*=' "$tree/Makefile" || true
fi

echo
echo "Potential S10+ defconfigs:"
find "$tree/arch/arm64/configs" -maxdepth 2 -type f \
  \( -iname '*beyond2lte*' -o -iname '*exynos9820*' -o -iname '*extreme*' \) \
  -print 2>/dev/null | sort || true

echo
echo "This check does not build, modify, package, or flash anything."
