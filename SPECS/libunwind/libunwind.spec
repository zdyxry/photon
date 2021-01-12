Summary:        Portable and efficient C programming interface (API) to determine the call-chain of a program.
Name:           libunwind
Version:        1.4.0
Release:        2%{?dist}
License:        X11
URL:            http://www.nongnu.org/libunwind/
Source0:        http://download.savannah.gnu.org/releases/%{name}/%{name}-%{version}.tar.gz
%define sha1    libunwind=6bb7726f9f7440319bf8efc55e32281e2e39e7f4
Patch0:         libunwind-1.4-gcc-10.patch
Group:          Utilities/Libraries
Vendor:         VMware, Inc.
Distribution:   Photon

%description
Portable and efficient C programming interface (API) to determine the call-chain of a program. The API additionally provides the means to manipulate the preserved (callee-saved) state of each call-frame and to resume execution at any point in the call-chain (non-local goto). The API supports both local (same-process) and remote (across-process) operation. As such, the API is useful in a number of applications.

%package        devel
Summary:        libunwind devel
Group:          Development/Tools
Requires:       %{name} = %{version}-%{release}
%description    devel
This contains development tools and libraries for libunwind.

%prep
%setup -q
%patch0 -p1

%build
%configure \
	--disable-silent-rules
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install
find %{buildroot} -name '*.la' -delete

%files
%defattr(-,root,root)
%{_libdir}/libunwind*.so.*

%files devel
%{_includedir}/*unwind*
%{_libdir}/libunwind*.a
%{_libdir}/libunwind*.so
%{_libdir}/pkgconfig/libunwind*

%changelog
*   Wed Jan 13 2021 Alexey Makhalov <amakhalov@vmware.com> 1.4.0-2
-   GCC-10 support
*   Wed Aug 12 2020 Gerrit Photon <photon-checkins@vmware.com> 1.4.0-1
-   Automatic Version Bump
*   Sun Sep 29 2019 Srivatsa S. Bhat (VMware) <srivatsa@csail.mit.edu> 1.2-3
-   libunwind-devel needs libunwind.
*   Fri Oct 13 2017 Alexey Makhalov <amakhalov@vmware.com> 1.2-2
-   Use standard configure macros
*   Mon Feb 06 2017 Vinay Kulkarni <kulkarniv@vmware.com> 1.2-1
-   Initial version of libunwind package for Photon.
