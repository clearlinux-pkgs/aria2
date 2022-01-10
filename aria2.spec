#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : aria2
Version  : 1.36.0
Release  : 4
URL      : https://github.com/aria2/aria2/releases/download/release-1.36.0/aria2-1.36.0.tar.xz
Source0  : https://github.com/aria2/aria2/releases/download/release-1.36.0/aria2-1.36.0.tar.xz
Summary  : High speed download utility library
Group    : Development/Tools
License  : GPL-2.0 MIT OpenSSL
Requires: aria2-bin = %{version}-%{release}
Requires: aria2-license = %{version}-%{release}
Requires: aria2-locales = %{version}-%{release}
Requires: aria2-man = %{version}-%{release}
BuildRequires : CUnit-dev
BuildRequires : bison
BuildRequires : gmp-dev
BuildRequires : pkgconfig(cppunit)
BuildRequires : pkgconfig(expat)
BuildRequires : pkgconfig(gnutls)
BuildRequires : pkgconfig(jemalloc)
BuildRequires : pkgconfig(libcares)
BuildRequires : pkgconfig(libssh2)
BuildRequires : pkgconfig(libtcmalloc_minimal)
BuildRequires : pkgconfig(libuv)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(nettle)
BuildRequires : pkgconfig(openssl)
BuildRequires : pkgconfig(sqlite3)
BuildRequires : pkgconfig(zlib)
BuildRequires : pypi-sphinx

%description


%package bin
Summary: bin components for the aria2 package.
Group: Binaries
Requires: aria2-license = %{version}-%{release}

%description bin
bin components for the aria2 package.


%package doc
Summary: doc components for the aria2 package.
Group: Documentation
Requires: aria2-man = %{version}-%{release}

%description doc
doc components for the aria2 package.


%package license
Summary: license components for the aria2 package.
Group: Default

%description license
license components for the aria2 package.


%package locales
Summary: locales components for the aria2 package.
Group: Default

%description locales
locales components for the aria2 package.


%package man
Summary: man components for the aria2 package.
Group: Default

%description man
man components for the aria2 package.


%prep
%setup -q -n aria2-1.36.0
cd %{_builddir}/aria2-1.36.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641853409
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1641853409
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/aria2
cp %{_builddir}/aria2-1.36.0/COPYING %{buildroot}/usr/share/package-licenses/aria2/68c94ffc34f8ad2d7bfae3f5a6b996409211c1b1
cp %{_builddir}/aria2-1.36.0/LICENSE.OpenSSL %{buildroot}/usr/share/package-licenses/aria2/2b7ed594a25796f84812c487da49ea6f9260a979
cp %{_builddir}/aria2-1.36.0/deps/wslay/COPYING %{buildroot}/usr/share/package-licenses/aria2/244f0f3e67f4ed26ff65034c3db122d413cdef97
%make_install
%find_lang aria2

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/aria2c

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/aria2/*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/aria2/244f0f3e67f4ed26ff65034c3db122d413cdef97
/usr/share/package-licenses/aria2/2b7ed594a25796f84812c487da49ea6f9260a979
/usr/share/package-licenses/aria2/68c94ffc34f8ad2d7bfae3f5a6b996409211c1b1

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/aria2c.1
/usr/share/man/pt/man1/aria2c.1
/usr/share/man/ru/man1/aria2c.1

%files locales -f aria2.lang
%defattr(-,root,root,-)

