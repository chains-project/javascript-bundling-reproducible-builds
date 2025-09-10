#!/bin/sh -e

DOCKER="podman"

${DOCKER} load < $(nix-build oci_image1.nix)
${DOCKER} load < $(nix-build oci_image2.nix)
