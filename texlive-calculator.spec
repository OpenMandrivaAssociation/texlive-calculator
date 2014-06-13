# revision 33041
# category Package
# catalog-ctan /macros/latex/contrib/calculator
# catalog-date 2014-02-24 19:14:14 +0100
# catalog-license lppl1.2
# catalog-version 2.0
Name:		texlive-calculator
Version:	2.0
Release:	2
Summary:	Use LaTeX as a scientific calculator
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/calculator
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/calculator.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/calculator.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/calculator.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The calculator and calculus packages define several
instructions which allow us to realise algebraic operations and
to evaluate elementary functions and derivatives in our
documents. The package's main goal is to define the arithmetic
and functional calculations need in the author's package
xpicture, but the numeric abilities of "calculator" and
"calculus" may be useful in other contexts.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/calculator/calculator.sty
%{_texmfdistdir}/tex/latex/calculator/calculus.sty
%doc %{_texmfdistdir}/doc/latex/calculator/README
%doc %{_texmfdistdir}/doc/latex/calculator/calculator.pdf
%doc %{_texmfdistdir}/doc/latex/calculator/examples/calculator1.tex
%doc %{_texmfdistdir}/doc/latex/calculator/examples/calculator10.tex
%doc %{_texmfdistdir}/doc/latex/calculator/examples/calculator11.tex
%doc %{_texmfdistdir}/doc/latex/calculator/examples/calculator12.tex
%doc %{_texmfdistdir}/doc/latex/calculator/examples/calculator13.tex
%doc %{_texmfdistdir}/doc/latex/calculator/examples/calculator14.tex
%doc %{_texmfdistdir}/doc/latex/calculator/examples/calculator15.tex
%doc %{_texmfdistdir}/doc/latex/calculator/examples/calculator16.tex
%doc %{_texmfdistdir}/doc/latex/calculator/examples/calculator17.tex
%doc %{_texmfdistdir}/doc/latex/calculator/examples/calculator18.tex
%doc %{_texmfdistdir}/doc/latex/calculator/examples/calculator19.tex
%doc %{_texmfdistdir}/doc/latex/calculator/examples/calculator2.tex
%doc %{_texmfdistdir}/doc/latex/calculator/examples/calculator20.tex
%doc %{_texmfdistdir}/doc/latex/calculator/examples/calculator21.tex
%doc %{_texmfdistdir}/doc/latex/calculator/examples/calculator22.tex
%doc %{_texmfdistdir}/doc/latex/calculator/examples/calculator23.tex
%doc %{_texmfdistdir}/doc/latex/calculator/examples/calculator24.tex
%doc %{_texmfdistdir}/doc/latex/calculator/examples/calculator25.tex
%doc %{_texmfdistdir}/doc/latex/calculator/examples/calculator26.tex
%doc %{_texmfdistdir}/doc/latex/calculator/examples/calculator27.tex
%doc %{_texmfdistdir}/doc/latex/calculator/examples/calculator28.tex
%doc %{_texmfdistdir}/doc/latex/calculator/examples/calculator29.tex
%doc %{_texmfdistdir}/doc/latex/calculator/examples/calculator3.tex
%doc %{_texmfdistdir}/doc/latex/calculator/examples/calculator30.tex
%doc %{_texmfdistdir}/doc/latex/calculator/examples/calculator31.tex
%doc %{_texmfdistdir}/doc/latex/calculator/examples/calculator32.tex
%doc %{_texmfdistdir}/doc/latex/calculator/examples/calculator33.tex
%doc %{_texmfdistdir}/doc/latex/calculator/examples/calculator34.tex
%doc %{_texmfdistdir}/doc/latex/calculator/examples/calculator35.tex
%doc %{_texmfdistdir}/doc/latex/calculator/examples/calculator36.tex
%doc %{_texmfdistdir}/doc/latex/calculator/examples/calculator37.tex
%doc %{_texmfdistdir}/doc/latex/calculator/examples/calculator38.tex
%doc %{_texmfdistdir}/doc/latex/calculator/examples/calculator39.tex
%doc %{_texmfdistdir}/doc/latex/calculator/examples/calculator4.tex
%doc %{_texmfdistdir}/doc/latex/calculator/examples/calculator40.tex
%doc %{_texmfdistdir}/doc/latex/calculator/examples/calculator41.tex
%doc %{_texmfdistdir}/doc/latex/calculator/examples/calculator42.tex
%doc %{_texmfdistdir}/doc/latex/calculator/examples/calculator43.tex
%doc %{_texmfdistdir}/doc/latex/calculator/examples/calculator44.tex
%doc %{_texmfdistdir}/doc/latex/calculator/examples/calculator45.tex
%doc %{_texmfdistdir}/doc/latex/calculator/examples/calculator46.tex
%doc %{_texmfdistdir}/doc/latex/calculator/examples/calculator47.tex
%doc %{_texmfdistdir}/doc/latex/calculator/examples/calculator48.tex
%doc %{_texmfdistdir}/doc/latex/calculator/examples/calculator49.tex
%doc %{_texmfdistdir}/doc/latex/calculator/examples/calculator5.tex
%doc %{_texmfdistdir}/doc/latex/calculator/examples/calculator50.tex
%doc %{_texmfdistdir}/doc/latex/calculator/examples/calculator51.tex
%doc %{_texmfdistdir}/doc/latex/calculator/examples/calculator52.tex
%doc %{_texmfdistdir}/doc/latex/calculator/examples/calculator53.tex
%doc %{_texmfdistdir}/doc/latex/calculator/examples/calculator54.tex
%doc %{_texmfdistdir}/doc/latex/calculator/examples/calculator55.tex
%doc %{_texmfdistdir}/doc/latex/calculator/examples/calculator56.tex
%doc %{_texmfdistdir}/doc/latex/calculator/examples/calculator57.tex
%doc %{_texmfdistdir}/doc/latex/calculator/examples/calculator58.tex
%doc %{_texmfdistdir}/doc/latex/calculator/examples/calculator59.tex
%doc %{_texmfdistdir}/doc/latex/calculator/examples/calculator6.tex
%doc %{_texmfdistdir}/doc/latex/calculator/examples/calculator60.tex
%doc %{_texmfdistdir}/doc/latex/calculator/examples/calculator61.tex
%doc %{_texmfdistdir}/doc/latex/calculator/examples/calculator62.tex
%doc %{_texmfdistdir}/doc/latex/calculator/examples/calculator7.tex
%doc %{_texmfdistdir}/doc/latex/calculator/examples/calculator8.tex
%doc %{_texmfdistdir}/doc/latex/calculator/examples/calculator9.tex
#- source
%doc %{_texmfdistdir}/source/latex/calculator/calculator.dtx
%doc %{_texmfdistdir}/source/latex/calculator/calculator.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
