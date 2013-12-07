# revision 27112
# category Package
# catalog-ctan /macros/latex/contrib/calculator
# catalog-date 2012-07-03 11:28:15 +0200
# catalog-license lppl1.2
# catalog-version 1.0a
Name:		texlive-calculator
Version:	1.0a
Release:	5
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
%doc %{_texmfdistdir}/doc/latex/calculator/calculator1.tex
%doc %{_texmfdistdir}/doc/latex/calculator/calculator10.tex
%doc %{_texmfdistdir}/doc/latex/calculator/calculator11.tex
%doc %{_texmfdistdir}/doc/latex/calculator/calculator12.tex
%doc %{_texmfdistdir}/doc/latex/calculator/calculator13.tex
%doc %{_texmfdistdir}/doc/latex/calculator/calculator14.tex
%doc %{_texmfdistdir}/doc/latex/calculator/calculator15.tex
%doc %{_texmfdistdir}/doc/latex/calculator/calculator16.tex
%doc %{_texmfdistdir}/doc/latex/calculator/calculator17.tex
%doc %{_texmfdistdir}/doc/latex/calculator/calculator18.tex
%doc %{_texmfdistdir}/doc/latex/calculator/calculator19.tex
%doc %{_texmfdistdir}/doc/latex/calculator/calculator2.tex
%doc %{_texmfdistdir}/doc/latex/calculator/calculator20.tex
%doc %{_texmfdistdir}/doc/latex/calculator/calculator21.tex
%doc %{_texmfdistdir}/doc/latex/calculator/calculator22.tex
%doc %{_texmfdistdir}/doc/latex/calculator/calculator23.tex
%doc %{_texmfdistdir}/doc/latex/calculator/calculator24.tex
%doc %{_texmfdistdir}/doc/latex/calculator/calculator25.tex
%doc %{_texmfdistdir}/doc/latex/calculator/calculator26.tex
%doc %{_texmfdistdir}/doc/latex/calculator/calculator27.tex
%doc %{_texmfdistdir}/doc/latex/calculator/calculator28.tex
%doc %{_texmfdistdir}/doc/latex/calculator/calculator29.tex
%doc %{_texmfdistdir}/doc/latex/calculator/calculator3.tex
%doc %{_texmfdistdir}/doc/latex/calculator/calculator30.tex
%doc %{_texmfdistdir}/doc/latex/calculator/calculator31.tex
%doc %{_texmfdistdir}/doc/latex/calculator/calculator32.tex
%doc %{_texmfdistdir}/doc/latex/calculator/calculator33.tex
%doc %{_texmfdistdir}/doc/latex/calculator/calculator34.tex
%doc %{_texmfdistdir}/doc/latex/calculator/calculator35.tex
%doc %{_texmfdistdir}/doc/latex/calculator/calculator36.tex
%doc %{_texmfdistdir}/doc/latex/calculator/calculator37.tex
%doc %{_texmfdistdir}/doc/latex/calculator/calculator38.tex
%doc %{_texmfdistdir}/doc/latex/calculator/calculator39.tex
%doc %{_texmfdistdir}/doc/latex/calculator/calculator4.tex
%doc %{_texmfdistdir}/doc/latex/calculator/calculator40.tex
%doc %{_texmfdistdir}/doc/latex/calculator/calculator41.tex
%doc %{_texmfdistdir}/doc/latex/calculator/calculator42.tex
%doc %{_texmfdistdir}/doc/latex/calculator/calculator43.tex
%doc %{_texmfdistdir}/doc/latex/calculator/calculator44.tex
%doc %{_texmfdistdir}/doc/latex/calculator/calculator45.tex
%doc %{_texmfdistdir}/doc/latex/calculator/calculator46.tex
%doc %{_texmfdistdir}/doc/latex/calculator/calculator47.tex
%doc %{_texmfdistdir}/doc/latex/calculator/calculator48.tex
%doc %{_texmfdistdir}/doc/latex/calculator/calculator49.tex
%doc %{_texmfdistdir}/doc/latex/calculator/calculator5.tex
%doc %{_texmfdistdir}/doc/latex/calculator/calculator50.tex
%doc %{_texmfdistdir}/doc/latex/calculator/calculator51.tex
%doc %{_texmfdistdir}/doc/latex/calculator/calculator52.tex
%doc %{_texmfdistdir}/doc/latex/calculator/calculator53.tex
%doc %{_texmfdistdir}/doc/latex/calculator/calculator54.tex
%doc %{_texmfdistdir}/doc/latex/calculator/calculator55.tex
%doc %{_texmfdistdir}/doc/latex/calculator/calculator56.tex
%doc %{_texmfdistdir}/doc/latex/calculator/calculator57.tex
%doc %{_texmfdistdir}/doc/latex/calculator/calculator6.tex
%doc %{_texmfdistdir}/doc/latex/calculator/calculator7.tex
%doc %{_texmfdistdir}/doc/latex/calculator/calculator8.tex
%doc %{_texmfdistdir}/doc/latex/calculator/calculator9.tex
#- source
%doc %{_texmfdistdir}/source/latex/calculator/calculator.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Thu Aug 09 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0a-1
+ Revision: 813425
- Import texlive-calculator
- Import texlive-calculator

