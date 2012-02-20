%global packname  Rcsdp
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          0.1_41
Release:          1
Summary:          R interface to the CSDP semidefinite programming library
Group:            Sciences/Mathematics
License:          file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-41.tar.gz
Requires:         R-Matrix 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex 
BuildRequires:    R-Matrix 
BuildRequires:    blas-devel
BuildRequires:    coin-or-devel
BuildRequires:    lapack-devel

%description
R interface to the CSDP semidefinite programming library. Installs version
6.0.1 of CSDP from the COIN-OR website if required. An existing
intallation of CSDP may be used by passing the proper configure arguments
to the installation command. See the INSTALL file for further details.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/INSTALL
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
