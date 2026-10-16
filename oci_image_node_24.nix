{ pkgs ? import ./pkgs.nix { }
, # pkgsLinux ? import ./pkgs.nix {}
}:
# https://ryantm.github.io/nixpkgs/builders/images/dockertools/
let
  node_image = pkgs.dockerTools.pullImage {
    imageName = "node";
    # node:24.14.1-bookworm
        imageDigest = "sha256:1c0c30ea9d4e20052cdc6e9e0d36b9006edd890bd1ebc4f826991f7587a389d1";
    # sha256 = "sha256-Ke3IRxmw+WSFE3Kt0/i7ryW2zIMGIVanNZeZ2/oaft4=";
    sha256 = "sha256-/qKHMoGUF/sBmQcl+Nso97teQ1vuDncg3TIFcA6KVSk=";

  };
in
let
  # https://nix.dev/tutorials/nixos/building-and-running-docker-images.html
  image = pkgs.dockerTools.buildImage {
    name = "rb-24-bookworm";
    tag = "latest";
    # fromImage = "docker.io/library/archlinux";
    fromImage = node_image;

    # https://ryantm.github.io/nixpkgs/builders/images/dockertools/
    # copyToRoot = pkgs.buildEnv {
    #   name = "x";
    #   paths = with pkgs; [ bash nodejs coreutils  ];
    #   pathsToLink = [ "/bin" ];
    # };
    # config = {
    #   Cmd =["ls" "/"];
    # };
    # includeNixDB=true;
  };
in
image
#node_image
