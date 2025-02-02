Summary:        Commit RPMs to an OSTree repository
Name:           rpm-ostree
Version:        2020.5
Release:        6%{?dist}
License:        LGPLv2+
URL:            https://github.com/projectatomic/rpm-ostree
Vendor:         VMware, Inc.
Distribution:   Photon
Source0:        https://github.com/projectatomic/rpm-ostree/releases/download/v%{version}/rpm-ostree-%{version}.tar.xz
%define sha1    rpm-ostree=42f76f192b64adb432abd8b1c2a7897e91fa835b
Source1:        libglnx-5ef78bb.tar.gz
%define sha1    libglnx=5acb68bdfe9dd9dc9f6c91a34c22fe5693631a7b
Source2:        libdnf-c87ff63.tar.gz
%define sha1    libdnf=58c9ebeeabe84ea6b263b1460e3ecb41e29d04c3
Source3:        mk-ostree-host.sh
Source4:        function.inc
Source5:        mkostreerepo
Patch0:         rpm-ostree-libdnf-build.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  check
BuildRequires:  cmake
BuildRequires:  libtool
BuildRequires:  git
BuildRequires:  json-glib-devel
BuildRequires:  json-c-devel
BuildRequires:  gtk-doc
BuildRequires:  libcap-devel
BuildRequires:  sqlite-devel
BuildRequires:  cppunit-devel
BuildRequires:  polkit-devel
BuildRequires:  ostree-devel
BuildRequires:  docbook-xsl
BuildRequires:  libxslt
BuildRequires:  gobject-introspection-devel
BuildRequires:  openssl-devel
BuildRequires:  rpm-devel
BuildRequires:  librepo-devel
BuildRequires:  attr-devel
BuildRequires:  python3-libs
BuildRequires:  python3
BuildRequires:  autogen
BuildRequires:  libsolv-devel >= 0.7.19
BuildRequires:  libsolv
BuildRequires:  systemd-devel
BuildRequires:  libarchive-devel
BuildRequires:  gperf
BuildRequires:  which
BuildRequires:  popt-devel
BuildRequires:  createrepo_c
BuildRequires:  photon-release
BuildRequires:  photon-repos
BuildRequires:  bubblewrap
BuildRequires:  dbus
BuildRequires:  rust
BuildRequires:  libmodulemd-devel
BuildRequires:  gpgme-devel

Requires:       libcap
Requires:       librepo
Requires:       openssl
Requires:       ostree
Requires:       ostree-libs
Requires:       ostree-grub2
Requires:       json-glib
Requires:       libsolv
Requires:       bubblewrap

%description
This tool takes a set of packages, and commits them to an OSTree
repository.  At the moment, it is intended for use on build servers.

%package devel
Summary: Development headers for rpm-ostree
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
Includes the header files for the rpm-ostree library.

%package host
Summary: File for rpm-ostree-host creation
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description host
Includes the scripts for rpm-ostree host creation

%package repo
Summary: File for Repo Creation to act as server
Group: Applications/System
Requires: %{name} = %{version}-%{release}

%description repo
Includes the scripts for rpm-ostree repo creation to act as server

%prep
%setup -q
tar -xf %{SOURCE1} --no-same-owner
tar -xf %{SOURCE2} --no-same-owner
%patch0 -p0

%build
env NOCONFIGURE=1 ./autogen.sh
%configure --disable-silent-rules --enable-gtk-doc
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} INSTALL="install -p -c"
find %{buildroot} -name '*.la' -delete
install -d %{buildroot}%{_bindir}/rpm-ostree-host
install -d %{buildroot}%{_bindir}/rpm-ostree-server
install -p -m 755 -D %{SOURCE3} %{buildroot}%{_bindir}/rpm-ostree-host
install -p -m 644 -D %{SOURCE4} %{buildroot}%{_bindir}/rpm-ostree-host
install -p -m 755 -D %{SOURCE5} %{buildroot}%{_bindir}/rpm-ostree-server

%files
%{_bindir}/*
%{_libdir}/%{name}/
%{_libdir}/*.so.1*
%{_libdir}/girepository-1.0/*.typelib
%{_unitdir}/*.service
%{_libexecdir}/*
%{_datadir}/dbus-1/system.d/*.conf
%{_datadir}/dbus-1/system-services/*
%config(noreplace) %{_sysconfdir}/rpm-ostreed.conf
%{_libdir}/systemd/system/rpm-ostreed-automatic.timer
%{_datadir}/bash-completion/completions/rpm-ostree
%{_datadir}/dbus-1/interfaces/org.projectatomic.rpmostree1.xml
%{_datadir}/polkit-1/actions/org.projectatomic.rpmostree1.policy
%{_mandir}/man1/rpm-ostree.1.gz
%{_mandir}/man5/rpm-ostreed*
%{_mandir}/man8/rpm-ostreed*

%files devel
%{_libdir}/lib*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_datadir}/gtk-doc/html/*
%{_datadir}/gir-1.0/*-1.0.gir

%files host
%{_bindir}/rpm-ostree-host/mk-ostree-host.sh
%{_bindir}/rpm-ostree-host/function.inc

%files repo
%{_bindir}/rpm-ostree-server/mkostreerepo

%changelog
*   Fri Jun 11 2021 Oliver Kurth <okurth@vmware.com> 2020.5-6
-   build with libsolv 0.7.19
*   Mon Jan 11 2021 Ankit Jain <ankitja@vmware.com> 2020.5-5
-   Added systemd-udev in mkostreerepo
*   Tue Nov 03 2020 Ankit Jain <ankitja@vmware.com> 2020.5-4
-   Adding grub2-efi-image for both x86 and aarch64 in mkostreerepo
*   Mon Oct 05 2020 Ankit Jain <ankitja@vmware.com> 2020.5-3
-   Changing branch to 4.0 in mkostreerepo
*   Mon Oct 05 2020 Ankit Jain <ankitja@vmware.com> 2020.5-2
-   Re-enabling ostree
*   Mon Sep 21 2020 Ankit Jain <ankitja@vmware.com> 2020.5-1
-   Updated to 2020.5
*   Tue Sep 08 2020 Ankit Jain <ankitja@vmware.com> 2020.4-2
-   Updated mkostreerepo as per photon-base.json
*   Thu Aug 13 2020 Ankit Jain <ankitja@vmware.com> 2020.4-1
-   Updated to 2020.4
*   Mon Jun 22 2020 Tapas Kundu <tkundu@vmware.com> 2019.3-4
-   Build with python3
-   Mass removal python2
*   Thu Oct 24 2019 Ankit Jain <ankitja@vmware.com> 2019.3-3
-   Added for ARM Build
*   Fri Sep 20 2019 Ankit Jain <ankitja@vmware.com> 2019.3-2
-   Added script to create repo data to act as ostree-server
*   Tue May 14 2019 Ankit Jain <ankitja@vmware.com> 2019.3-1
-   Initial version of rpm-ostree
