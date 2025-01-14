Name:		texlive-hrlatex
Version:	18020
Release:	2
Summary:	LaTeX support for Croatian documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/croatian/hrlatex
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hrlatex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hrlatex.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hrlatex.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package simplifies creation of new documents for the
(average) Croatian user. As an example, a class file hrdipl.cls
(designed for the graduation thesis at the University of
Zagreb) and sample thesis documents are included.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/hrlatex/fsbispit.cls
%{_texmfdistdir}/tex/latex/hrlatex/fsbmath.sty
%{_texmfdistdir}/tex/latex/hrlatex/hrlatex.sty
%doc %{_texmfdistdir}/doc/latex/hrlatex/README
%doc %{_texmfdistdir}/doc/latex/hrlatex/hrlatex.pdf
%doc %{_texmfdistdir}/doc/latex/hrlatex/sample.fsbispit.tex
%doc %{_texmfdistdir}/doc/latex/hrlatex/sample.minimal.cp1250.tex
%doc %{_texmfdistdir}/doc/latex/hrlatex/sample.minimal.latin2.tex
%doc %{_texmfdistdir}/doc/latex/hrlatex/sample.minimal.utf8.tex
%doc %{_texmfdistdir}/doc/latex/hrlatex/sample.prezentacija.tex
#- source
%doc %{_texmfdistdir}/source/latex/hrlatex/hrlatex.dtx
%doc %{_texmfdistdir}/source/latex/hrlatex/hrlatex.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
