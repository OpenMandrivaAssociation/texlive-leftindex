%global tl_name leftindex
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2beta
Release:	%{tl_revision}.1
Summary:	Left indices with better spacing
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/leftindex
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/leftindex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/leftindex.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides commands for typesetting left indices. Unlike
other similar packages, leftindex also indents the left superscript,
providing much better spacing in general.

