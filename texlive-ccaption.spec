Name:		texlive-ccaption
Version:	23443
Release:	2
Summary:	Continuation headings and legends for floats
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ccaption
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ccaption.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ccaption.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ccaption.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A package providing commands for 'continuation captions',
unnumbered captions, and also a non-specific legend heading for
any environment. Methods are also provided to define captions
for use outside float (e.g., figure and table) environments,
and to define new float environments and Lists of Floats. Tools
are provided for specifying your own captioning styles.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/ccaption/ccaption.sty
%doc %{_texmfdistdir}/doc/latex/ccaption/README
%doc %{_texmfdistdir}/doc/latex/ccaption/ccaption.pdf
#- source
%doc %{_texmfdistdir}/source/latex/ccaption/ccaption.dtx
%doc %{_texmfdistdir}/source/latex/ccaption/ccaption.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
