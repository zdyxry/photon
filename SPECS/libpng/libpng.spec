Summary:	contains libraries for reading and writing PNG files.
Name:		libpng
Version:	1.6.27
Release:	2%{?dist}
License:	libpng
URL:		http://www.libpng.org/
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://downloads.sourceforge.net/libpng/%{name}-%{version}.tar.xz
Patch0:		libpng-CVE-2019-7317.patch
%define sha1 libpng=af5d742f5d0a6492133aed7790bb43e8854cca64
Provides:	pkgconfig(libpng)
Provides:	pkgconfig(libpng16)
%description
The libpng package contains libraries used by other programs for reading and writing PNG files. The PNG format was designed as a replacement for GIF and, to a lesser extent, TIFF, with many improvements and extensions and lack of patent problems.

%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}-%{release}
%description	devel
It contains the libraries and header files to create applications 

%prep
%setup -q
%patch0 -p1
%build
./configure \
	--prefix=%{_prefix} \
	--disable-static
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install
find %{buildroot} -name '*.la' -delete

%check
make %{?_smp_mflags} -k check

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/*.so.*
%{_datadir}/*

%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
*	Fri May 10 2019 Harinadh Dommaraju <hdommaraju@vmware.com> 1.6.27-2
-	Fix for CVE-2019-7317
*       Thu Feb 23 2017 Divya Thaluru <dthaluru@vmware.com> 1.6.27-1
-       Updated to version 1.6.27
*       Mon Sep 12 2016 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 1.6.23-2
-       Included the libpng16 pkgconfig 
*       Wed Jul 27 2016 Divya Thaluru <dthaluru@vmware.com> 1.6.23-1
-       Initial version
