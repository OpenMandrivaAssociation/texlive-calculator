Name:		texlive-calculator
Version:	64424
Release:	1
Summary:	Use LaTeX as a scientific calculator
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/calculator
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/calculator.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/calculator.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/calculator.source.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/latex/calculator
%doc %{_texmfdistdir}/doc/latex/calculator
#- source
%doc %{_texmfdistdir}/source/latex/calculator

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
