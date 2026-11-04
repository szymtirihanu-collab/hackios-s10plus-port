#!/usr/bin/env bash
# Read-only host inventory for the HackiOS S10+ kernel research project.
set -u

printf '%s\n' "== Host =="
uname -a
printf '\n%s\n' "== Distribution =="
if [ -r /etc/os-release ]; then
  . /etc/os-release
  printf 'NAME=%s\nVERSION=%s\n' "${NAME:-unknown}" "${VERSION_ID:-unknown}"
else
  printf '%s\n' "/etc/os-release not found"
fi

printf '\n%s\n' "== Available build tools =="
for tool in git make gcc clang ld.lld python3 perl bc flex bison openssl dtc; do
  if command -v "$tool" >/dev/null 2>&1; then
    printf '%-10s %s\n' "$tool" "$(command -v "$tool")"
  else
    printf '%-10s %s\n' "$tool" "not found"
  fi
done

printf '\n%s\n' "== Cross-compilers =="
for tool in aarch64-linux-gnu-gcc aarch64-linux-gnu-g++ aarch64-linux-gnu-ld llvm-ar; do
  if command -v "$tool" >/dev/null 2>&1; then
    printf '%-24s %s\n' "$tool" "$(command -v "$tool")"
  else
    printf '%-24s %s\n' "$tool" "not found"
  fi
done

printf '\n%s\n' "This script only reports host information; it does not install packages or modify the device.\n"
