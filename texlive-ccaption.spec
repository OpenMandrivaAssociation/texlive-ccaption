%global tl_name ccaption
%global tl_revision 79461

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.2c
Release:	%{tl_revision}.1
Summary:	Continuation headings and legends for floats
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ccaption
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ccaption.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ccaption.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ccaption.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A package providing commands for 'continuation captions', unnumbered
captions, and also a non-specific legend heading for any environment.
Methods are also provided to define captions for use outside float
(e.g., figure and table) environments, and to define new float
environments and Lists of Floats. Tools are provided for specifying your
own captioning styles.

