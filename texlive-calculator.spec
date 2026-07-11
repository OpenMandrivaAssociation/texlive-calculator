%global tl_name calculator
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.1
Release:	%{tl_revision}.1
Summary:	Use LaTeX as a scientific calculator
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/calculator
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/calculator.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/calculator.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/calculator.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The calculator and calculus packages define several instructions which
allow us to realise algebraic operations and to evaluate elementary
functions and derivatives in our documents. The package's main goal is
to define the arithmetic and functional calculations needed in the
author's package xpicture, but the numeric abilities of "calculator" and
"calculus" may be useful in other contexts.

