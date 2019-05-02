Name:           vncsnapshot
Version:        1.2a
Release:        xs18%{?dist}
Epoch:          0
Summary:        VNC Snapshot is a command-line program for VNC. It will save a JPEG image of the VNC server's screen.

Group:          Application/Productivity
License:        GPL
URL:            http://vncsnapshot.sourceforge.net/

Source0: https://repo.citrite.net/xs-local-contrib/vncsnapshot/vncsnapshot-1.2a-src.tar.bz2
Patch0: SOURCES/vncsnapshot/vnc-format.patch
Patch1: SOURCES/vncsnapshot/vnc-multi-overflow.patch
Patch2: SOURCES/vncsnapshot/vnc-snapshot-multi.patch
Patch3: SOURCES/vncsnapshot/vnc-64bit.patch
Patch4: SOURCES/vncsnapshot/vnc-only-cursor.patch
Patch5: SOURCES/vncsnapshot/add-unix-socket-support.patch


Provides: gitsha(https://code.citrite.net/rest/archive/latest/projects/XS/repos/vncsnapshot/archive?at=1.0.1&format=tar#/vncsnapshot.patches.tar) = cd16f076aac2791b6e994767ea1f4dc851cc3313

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

BuildRequires:  gcc-c++
BuildRequires:  zlib-devel >= 1.2
BuildRequires:  libjpeg-devel
Requires:       zlib >= 1.2
Requires:       libjpeg

%description
Snapshot is a command-line program for VNC. It will save a JPEG image of the VNC server's screen.

Also included with the package is vncpasswd, to allow you to create password files if you do not have a Unix or Linux version of VNC available. Note that while this utility is in the Windows version of VNC Snapshot, it does not create a file usable by the Windows version of the VNC Server.

VNC Snapshot is derived from Tight VNC [www.tightvnc.com] and Real VNC [www.realvnc.com].


%prep
%setup -q -n %{name}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
make

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1

cp -ar vncsnapshot %{buildroot}%{_bindir}
cp -ar vncpasswd %{buildroot}%{_bindir}/vncpassword-vncsnapshot

cat vncsnapshot.man1 | gzip -c > %{buildroot}%{_mandir}/man1/vncsnapshot.1.gz

%clean
rm -rf %{buildroot} 

%files 
%defattr(-,root,root,-)
%doc BUILD BUILD.unix BUILD.win32 CHANGE-LOG.txt MANIFEST README RELEASE-NOTES-1.1.txt RELEASE-NOTES.txt web-page.html
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Thu Nov 02 2017 Ross Lagerwall <ross.lagerwall@citrix.com> - 1.2a-xs18
- Add support for connecting to a UNIX socket.

* Fri Mar 23 2012 Citrix Systems, Inc. <www.citrix.com>
- fix possible buffer overflow if many images are captured
- fix format error
- does not take capture twice
* Wed Jun 06 2006 Citrix Systems, Inc. <www.citrix.com>
- modified for XenServer
* Fri Oct 01 2004 Casper Pedersen <cpedersen[AT]c-note.dk> - 0:1.2a
- Initial RPM release.
