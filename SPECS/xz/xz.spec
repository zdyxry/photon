Summary:        Programs for compressing and decompressing files
Name:           xz
Version:        5.2.4
Release:        1%{?dist}
URL:            http://tukaani.org/xz
License:        GPLv2+ and GPLv3+ and LGPLv2+
Group:          Applications/File
Vendor:         VMware, Inc.
Distribution:   Photon
Source0:        http://tukaani.org/xz/%{name}-%{version}.tar.xz
%define sha1    xz=1d3a6910c28d40df0134f4a49e5570e8249120c5
Requires:       xz-libs = %{version}-%{release}
%description
The Xz package contains programs for compressing and
decompressing files

%package lang
Summary: Additional language files for xz
Group:      Applications/File
Requires: %{name} = %{version}-%{release}
%description lang
These are the additional language files of xz.

%package    devel
Summary:    Header and development files for xz
Requires:   %{name} = %{version}-%{release}
%description    devel
It contains the libraries and header files to create applications

%package libs
Summary: Libraries for xz
Group:      System Environment/Libraries
%description libs
This package contains minimal set of shared xz libraries.

%prep
%setup -q
%build
./configure \
    --prefix=%{_prefix} \
    --docdir=%{_defaultdocdir}/%{name}-%{version} \
    --disable-static \
    --disable-silent-rules
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} pkgconfigdir=%{_libdir}/pkgconfig install
install -vdm 755 %{buildroot}/{bin,%_lib}
mv -v   %{buildroot}%{_bindir}/{lzma,unlzma,lzcat,xz,unxz,xzcat} %{buildroot}/bin
ln -svf "../..%{_lib}/$(readlink %{buildroot}%{_libdir}/liblzma.so)" %{buildroot}%{_libdir}/liblzma.so
find %{buildroot}%{_libdir} -name '*.la' -delete
%find_lang %{name}
%check
make  %{?_smp_mflags}  check

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
/bin/xz
/bin/lzcat
/bin/lzma
/bin/xzcat
/bin/unlzma
/bin/unxz
%{_bindir}/xzless
%{_bindir}/lzmadec
%{_bindir}/xzcmp
%{_bindir}/lzegrep
%{_bindir}/lzcmp
%{_bindir}/xzfgrep
%{_bindir}/xzmore
%{_bindir}/lzgrep
%{_bindir}/xzdiff
%{_bindir}/lzfgrep
%{_bindir}/xzegrep
%{_bindir}/lzless
%{_bindir}/lzdiff
%{_bindir}/lzmore
%{_bindir}/lzmainfo
%{_bindir}/xzgrep
%{_bindir}/xzdec
%{_mandir}/man1/*

%files devel
%{_includedir}/lzma.h
%{_includedir}/lzma/*.h
%{_libdir}/pkgconfig/liblzma.pc
%{_libdir}/liblzma.so
%{_defaultdocdir}/%{name}-%{version}/*

%files libs
%{_libdir}/liblzma.so.*

%files lang -f %{name}.lang
%defattr(-,root,root)

%changelog
*   Thu Sep 13 2018 Siju Maliakkal <smaliakkal@vmware.com> 5.2.4-1
-   Updated to latest version
*   Fri Apr 14 2017 Alexey Makhalov <amakhalov@vmware.com> 5.2.3-2
-   Added -libs subpackage. Disable static.
*   Wed Apr 05 2017 Xiaolin Li <xiaolinl@vmware.com> 5.2.3-1
-   Updated to version 5.2.3.
*   Wed Nov 23 2016 Alexey Makhalov <amakhalov@vmware.com> 5.2.2-4
-   Added -lang subpackage
*   Wed Oct 05 2016 ChangLee <changlee@vmware.com> 5.2.2-3
-   Modified %check
*   Tue May 24 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 5.2.2-2
-   GA - Bump release of all rpms
*   Wed Jan 20 2016 Anish Swaminathan <anishs@vmware.com> 5.2.2-1
-   Upgrade version.
*   Mon May 18 2015 Touseef Liaqat <tliaqat@vmware.com> 5.0.5-2
-   Update according to UsrMove.
*   Wed Nov 5 2014 Divya Thaluru <dthaluru@vmware.com> 5.0.5-1
-   Initial build. First version
