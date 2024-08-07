#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v13
# autospec commit: dc0ff31
#
Name     : aria2
Version  : 1.37.0
Release  : 6
URL      : https://github.com/aria2/aria2/releases/download/release-1.37.0/aria2-1.37.0.tar.gz
Source0  : https://github.com/aria2/aria2/releases/download/release-1.37.0/aria2-1.37.0.tar.gz
Summary  : High speed download utility library
Group    : Development/Tools
License  : GPL-2.0 MIT OpenSSL
Requires: aria2-bin = %{version}-%{release}
Requires: aria2-license = %{version}-%{release}
Requires: aria2-locales = %{version}-%{release}
Requires: aria2-man = %{version}-%{release}
BuildRequires : CUnit-dev
BuildRequires : bison
BuildRequires : buildreq-configure
BuildRequires : file
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
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
%setup -q -n aria2-1.37.0
cd %{_builddir}/aria2-1.37.0
pushd ..
cp -a aria2-1.37.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1719951321
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%configure --disable-static
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%configure --disable-static
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check || :
cd ../buildavx2;
make %{?_smp_mflags} check || : || :

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1719951321
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/aria2
cp %{_builddir}/aria2-%{version}/COPYING %{buildroot}/usr/share/package-licenses/aria2/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/aria2-%{version}/LICENSE.OpenSSL %{buildroot}/usr/share/package-licenses/aria2/2b7ed594a25796f84812c487da49ea6f9260a979 || :
cp %{_builddir}/aria2-%{version}/deps/wslay/COPYING %{buildroot}/usr/share/package-licenses/aria2/244f0f3e67f4ed26ff65034c3db122d413cdef97 || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v2
%make_install
%find_lang aria2
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/aria2c
/usr/bin/aria2c

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/aria2/*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/aria2/244f0f3e67f4ed26ff65034c3db122d413cdef97
/usr/share/package-licenses/aria2/2b7ed594a25796f84812c487da49ea6f9260a979
/usr/share/package-licenses/aria2/4cc77b90af91e615a64ae04893fdffa7939db84c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/aria2c.1
/usr/share/man/pt/man1/aria2c.1
/usr/share/man/ru/man1/aria2c.1

%files locales -f aria2.lang
%defattr(-,root,root,-)

