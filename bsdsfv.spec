Summary:	Utility for handling .sfv checksum files
Summary(pl):	Narzêdzie do obs³ugi plików .sfv zawieraj±cych sumy kontrolne
Name:		bsdsfv
Version:	1.18
Release:	1
License:	unknown
Group:		Applications/File
Source0:	http://dl.sourceforge.net/sourceforge/bsdsfv/%{name}-%{version}.tar.gz
# Source0-md5:	381df19a827d5a20097ab95ea9e760fa
Patch0:		%{name}-manual.patch
URL:		http://bsdsfv.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Small utility for creating .sfv checksums. It also allows testing
files against existing .sfv checksums. Program is using CRC32
algorithm.

%description -l pl
Niewielkie narzêdzie do tworzenia sum kontrolnych w formacie .sfv.
Pozwala równie¿ na testowanie plików w oparciu o istniej±ce sumy
kontrolne. Program u¿ywa algorytmu CRC32.

%prep
%setup -q -n %{name}
%patch -p0

%build
%{__make} \
    CFLAGS="%{rpmcflags}" \
    CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install %{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README MANUAL
%attr(755,root,root) %{_bindir}/*
