#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-coveralls
Version  : 2.9.3
Release  : 7
URL      : https://files.pythonhosted.org/packages/a2/55/9db73eeecbb832252e763dc66aa60551fb4560deffda493b56e83602429c/python-coveralls-2.9.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/a2/55/9db73eeecbb832252e763dc66aa60551fb4560deffda493b56e83602429c/python-coveralls-2.9.3.tar.gz
Summary  : Provide Seemless integration with coveralls.io
Group    : Development/Tools
License  : Apache-2.0
Requires: python-coveralls-bin = %{version}-%{release}
Requires: python-coveralls-license = %{version}-%{release}
Requires: python-coveralls-python = %{version}-%{release}
Requires: python-coveralls-python3 = %{version}-%{release}
Requires: PyYAML
Requires: coverage
Requires: requests
Requires: six
BuildRequires : PyYAML
BuildRequires : buildreq-distutils3
BuildRequires : coverage
BuildRequires : requests
BuildRequires : six

%description
====================================
Python interface to coveralls.io API
====================================

%package bin
Summary: bin components for the python-coveralls package.
Group: Binaries
Requires: python-coveralls-license = %{version}-%{release}

%description bin
bin components for the python-coveralls package.


%package license
Summary: license components for the python-coveralls package.
Group: Default

%description license
license components for the python-coveralls package.


%package python
Summary: python components for the python-coveralls package.
Group: Default
Requires: python-coveralls-python3 = %{version}-%{release}

%description python
python components for the python-coveralls package.


%package python3
Summary: python3 components for the python-coveralls package.
Group: Default
Requires: python3-core

%description python3
python3 components for the python-coveralls package.


%prep
%setup -q -n python-coveralls-2.9.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1564763961
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/python-coveralls
cp LICENSE %{buildroot}/usr/share/package-licenses/python-coveralls/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/coveralls

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/python-coveralls/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
