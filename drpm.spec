Name:           drpm
Version:        0.3.0
Release:        5%{?dist}
Summary:        A library for making, reading and applying deltarpm packages

# the entire source code is LGPLv3+, except src/drpm_diff.c and src/drpm_search.c which are BSD
License:        LGPLv3+ and BSD
URL:            https://fedorahosted.org/%{name}
Source:         https://fedorahosted.org/released/%{name}/%{name}-%{version}.tar.bz2

# add workaround for gcc7 on ppc64le temporary before it's fixed in gcc
# https://bugzilla.redhat.com/show_bug.cgi?id=1420350
Patch1:         drpm-0.3.0-workaround-ppc64le-gcc.patch

BuildRequires:  cmake >= 2.8
BuildRequires:  gcc

BuildRequires:  rpm-devel
BuildRequires:  openssl-devel
BuildRequires:  zlib-devel
BuildRequires:  bzip2-devel
BuildRequires:  xz-devel

BuildRequires:  pkgconfig
BuildRequires:  doxygen

BuildRequires:  libcmocka-devel >= 1.0
%ifarch %{ix86} x86_64 ppc ppc64 ppc64le s390x armv7hl aarch64
BuildRequires:  valgrind
%endif

%description
The drpm package provides a library for making, reading and applying deltarpms,
compatible with the original deltarpm packages.

%package devel
Summary:        C interface for the drpm library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The drpm-devel package provides a C interface (drpm.h) for the drpm library.

%prep
%autosetup -p1
mkdir build

%build
pushd build
%cmake ..
%make_build
make doc
popd

%install
pushd build
%make_install
popd

%check
pushd build
ctest -VV
popd

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license COPYING COPYING.LESSER LICENSE.BSD
%{_libdir}/libdrpm.so.*

%files devel
%doc build/doc/html/
%{_libdir}/libdrpm.so
%{_includedir}/drpm.h
%{_libdir}/pkgconfig/drpm.pc

%changelog
* Tue Mar 28 2017 Than Ngo <than@redhat.com> - 0.3.0-5
- added workaround for gcc7 bug on ppc64le temporary

* Thu Sep 29 2016 Pete Walter <pwalter@fedoraproject.org> - 0.3.0-4
- Simplify spec file

* Tue May 3 2016 Matej Chalk <mchalk@redhat.com> 0.3.0-3
- Now contains makedeltarpm and applydeltarpm functionality
- Added lzlib-devel dependency for OpenSUSE

* Tue Apr 12 2016 Igor Gnatenko <ignatenko@redhat.com> - 0.3.0-2
- Cleanup spec
- Make build out-of-tree
- Sync with valgrind arches
- Build documentation

* Thu Sep 3 2015 Matej Chalk <mchalk@redhat.com> 0.3.0-1
- Bumped minor version (deltarpm creation added)

* Tue Aug 4 2015 Matej Chalk <mchalk@redhat.com> 0.2.1-1
- Added openssl dependency

* Fri Jul 24 2015 Matej Chalk <mchalk@redhat.com> 0.2.0-2
- Fixed bug in test suite

* Tue Jun 23 2015 Matej Chalk <mchalk@redhat.com> 0.2.0-1
- Bumped minor version

* Fri Jun 19 2015 Matej Chalk <mchalk@redhat.com> 0.1.3-4
- Memory test only for architectures that have valgrind (#1232157)

* Wed Mar 11 2015 Matej Chalk <mchalk@redhat.com> 0.1.3-3
- Added cmocka and valgrind package dependencies

* Fri Mar 6 2015 Matej Chalk <mchalk@redhat.com> 0.1.3-2
- Added check section

* Fri Feb 13 2015 Matej Chalk <mchalk@redhat.com> 0.1.3-1
- Bumped version to 0.1.3
- Added CMake tool

* Fri Dec 19 2014 Matej Chalk <mchalk@redhat.com> 0.1.2-4
- Enabled hardened build

* Mon Dec 15 2014 Matej Chalk <mchalk@redhat.com> 0.1.2-3
- Added unversioned .so to package to enable linking with -ldrpm

* Thu Dec 11 2014 Matej Chalk <mchalk@redhat.com> 0.1.2-2
- Removed unversioned .so from package
- Included copies of both GPLv3 and LGPLv3

* Wed Dec 3 2014 Matej Chalk <mchalk@redhat.com> 0.1.2-1
- Bumped version to 0.1.2
- Added drpm.pc file for pkgconfig tool

* Thu Nov 6 2014 Matej Chalk <mchalk@redhat.com> 0.1.1-1
- Bumped version to 0.1.1

* Wed Nov 5 2014 Matej Chalk <mchalk@redhat.com> 0.1.0-1
- Initial RPM release
