Name:		texlive-leftindex
Version:	56182
Release:	2
Summary:	Left indices with better spacing
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/leftindex
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/leftindex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/leftindex.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides commands for typesetting left indices.
Unlike other similar packages, leftindex also indents the left
superscript, providing much better spacing in general.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/leftindex
%doc %{_texmfdistdir}/doc/latex/leftindex

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
