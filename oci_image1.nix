{ pkgs ? import ./pkgs.nix { }
, # pkgsLinux ? import ./pkgs.nix {}
}:
# https://ryantm.github.io/nixpkgs/builders/images/dockertools/
let
  node_image = pkgs.dockerTools.pullImage {
    imageName = "node";
    # lts-jod, node 22 and bookworm
    imageDigest = "sha256:37ff334612f77d8f999c10af8797727b731629c26f2e83caa6af390998bdc49c";
    sha256 = "sha256-Ke3IRxmw+WSFE3Kt0/i7ryW2zIMGIVanNZeZ2/oaft4=";

  };
in
let
  # https://nix.dev/tutorials/nixos/building-and-running-docker-images.html
  image = pkgs.dockerTools.buildImage {
    name = "rb-lts-jod";
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
