# revision 23443
# category Package
# catalog-ctan /macros/latex/contrib/ccaption
# catalog-date 2009-09-02 11:33:10 +0200
# catalog-license lppl1.3
# catalog-version 3.2b
Name:		texlive-ccaption
Version:	3.2b
Release:	7
Summary:	Continuation headings and legends for floats
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ccaption
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ccaption.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ccaption.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ccaption.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 3.2b-2
+ Revision: 750040
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 3.2b-1
+ Revision: 718017
- texlive-ccaption
- texlive-ccaption
- texlive-ccaption
- texlive-ccaption
- texlive-ccaption

