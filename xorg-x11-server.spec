# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.25
# 

Name:       xorg-x11-server

# >> macros
# << macros

Summary:    X.Org X11 X server
Version:    1.13.0
Release:    1
Group:      System/X11
License:    MIT
URL:        http://cgit.freedesktop.org/xorg/xserver
Source0:    http://xorg.freedesktop.org/archive/individual/xserver/xorg-server-%{version}.tar.bz2
Source100:  xorg-x11-server.yaml
Patch0:     cache-xkbcomp-output-for-fast-start-up.patch
Requires:   libdrm >= 2.4.0
BuildRequires:  pkgconfig(xorg-macros) >= 1.14
BuildRequires:  pkgconfig(fontutil) >= 1.1
BuildRequires:  pkgconfig(videoproto)
BuildRequires:  pkgconfig(compositeproto) >= 0.4
BuildRequires:  pkgconfig(recordproto) >= 1.13.99.1
BuildRequires:  pkgconfig(scrnsaverproto) >= 1.1
BuildRequires:  pkgconfig(resourceproto) >= 1.2.0
BuildRequires:  pkgconfig(xf86driproto) >= 2.1.0
BuildRequires:  pkgconfig(dri2proto) >= 2.8
BuildRequires:  pkgconfig(xineramaproto)
BuildRequires:  pkgconfig(xf86bigfontproto) >= 1.2.0
BuildRequires:  pkgconfig(xf86dgaproto) >= 2.0.99.1
BuildRequires:  pkgconfig(dmxproto) >= 2.2.99.1
BuildRequires:  pkgconfig(xf86vidmodeproto) >= 2.2.99.1
BuildRequires:  pkgconfig(xproto) >= 7.0.22
BuildRequires:  pkgconfig(randrproto) >= 1.4.0
BuildRequires:  pkgconfig(renderproto) >= 0.11
BuildRequires:  pkgconfig(xextproto) >= 7.1.99
BuildRequires:  pkgconfig(inputproto) >= 2.1.99.6
BuildRequires:  pkgconfig(kbproto) >= 1.0.3
BuildRequires:  pkgconfig(fontsproto)
BuildRequires:  pkgconfig(fixesproto) >= 5.0
BuildRequires:  pkgconfig(damageproto) >= 1.1
BuildRequires:  pkgconfig(xcmiscproto) >= 1.2.0
BuildRequires:  pkgconfig(bigreqsproto) >= 1.1.0
BuildRequires:  pkgconfig(xtrans) >= 1.2.2
BuildRequires:  pkgconfig(dmx) >= 1.0.99.1
BuildRequires:  pkgconfig(dri) >= 7.8.0
BuildRequires:  pkgconfig(libdrm) >= 2.3.0
BuildRequires:  pkgconfig(gl) >= 7.1.0
BuildRequires:  pkgconfig(xext) >= 1.0.99.4
BuildRequires:  pkgconfig(xfont) >= 1.4.2
BuildRequires:  pkgconfig(xi) >= 1.2.99.1
BuildRequires:  pkgconfig(xtst) >= 1.0.99.2
BuildRequires:  pkgconfig(pciaccess) >= 0.12.901
BuildRequires:  pkgconfig(libudev) >= 143
BuildRequires:  pkgconfig(dbus-1) >= 1.0
BuildRequires:  pkgconfig(pixman-1) >= 0.21.8
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  pkgconfig(glproto) >= 1.4.16
BuildRequires:  pkgconfig(xdmcp)
BuildRequires:  pkgconfig(xv)

%description
Description: %{summary}


%package devel
Summary:    SDK for X server driver module development
Group:      System/X11
Requires:   %{name} = %{version}-%{release}
Requires:   xorg-x11-util-macros
Requires:   pixman-devel
Requires:   libpciaccess-devel
Requires:   xorg-x11-proto-resourceproto
Requires:   xorg-x11-proto-scrnsaverproto
Requires:   xorg-x11-proto-xextproto
Requires:   xorg-x11-proto-xf86bigfontproto
Requires:   xorg-x11-proto-kbproto
Requires:   xorg-x11-proto-videoproto

%description devel
The SDK package provides the developmental files which are necessary for
developing X server driver modules, and for compiling driver modules
outside of the standard X11 source code tree.  Developers writing video
drivers, input drivers, or other X modules should install this package.


%package common
Summary:    Xorg server common files
Group:      System/X11
Requires:   %{name} = %{version}-%{release}

%description common
Common files shared among all X servers.

%package Xorg
Summary:    Xorg X server
Group:      System/X11
Requires:   %{name} = %{version}-%{release}
Requires:   xorg-x11-drv-mouse
Requires:   xorg-x11-drv-keyboard
Requires:   xorg-x11-drv-evdev
Requires:   xkbdata
Requires:   xkbcomp
Requires:   xorg-x11-server-common >= %{version}-%{release}
Conflicts:   %{name}-Xorg-setuid

%description Xorg
X.org X11 is an open source implementation of the X Window System.  It
provides the basic low level functionality which full fledged
graphical user interfaces (GUIs) such as GNOME and KDE are designed
upon.


%package Xorg-setuid
Summary:    Xorg X server with setuid
Group:      System/X11
Requires:   %{name} = %{version}-%{release}
Requires:   xorg-x11-drv-mouse
Requires:   xorg-x11-drv-keyboard
Requires:   xorg-x11-drv-evdev
Requires:   xkbdata
Requires:   xkbcomp
Requires:   xorg-x11-server-common >= %{version}-%{release}
Provides:   xorg-x11-server-Xorg = %{version}

%description Xorg-setuid
X.org X11 is an open source implementation of the X Window System.  It
provides the basic low level functionality which full fledged
graphical user interfaces (GUIs) such as GNOME and KDE are designed
upon.



%prep
%setup -q -n xorg-server-%{version}

# cache-xkbcomp-output-for-fast-start-up.patch
%patch0 -p1
# >> setup
# << setup

%build
# >> build pre
# << build pre

%reconfigure --disable-static \
    --enable-maintainer-mode \
    --enable-config-udev \
    --disable-config-hal \
    --disable-xvfb \
    --disable-xnest \
    --disable-dmx \
    --enable-glx \
    --enable-kdrive \
    --disable-xephyr \
    --disable-xfake \
    --disable-xfbdev \
    --enable-xorg \
    --with-pic \
    --with-default-font-path="catalogue:/etc/X11/fontpath.d,built-ins" \
    --with-module-dir=%{_libdir}/xorg/modules \
    --with-builderstring="Build ID: %{name} %{version}-%{release}" \
    --with-xkb-output=%{_localstatedir}/cache/xkb \
    --disable-xselinux \
    --disable-xinerama \
    --enable-dri2 \
    --enable-dri

make %{?jobs:-j%jobs}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
mkdir -p %{buildroot}/%{_sysconfdir}/X11/xorg.conf.d/
# << install post


%files
%defattr(-,root,root,-)
# >> files
# this section/file is intentionally left blank
# << files

%files devel
%defattr(-,root,root,-)
# >> files devel
%{_libdir}/pkgconfig/xorg-server.pc
%dir %{_includedir}/xorg
%{_includedir}/xorg/*.h
%{_datadir}/aclocal/xorg-server.m4
# << files devel

%files common
%defattr(-,root,root,-)
# >> files common
%doc %{_mandir}/man1/Xserver.1*
%{_libdir}/xorg/protocol.txt
# dir for caching xkb comp results, must be writable by non-root users
%dir %attr(777,-,-) %{_localstatedir}/cache/xkb
%attr(644,-,-) %{_localstatedir}/cache/xkb/README.compiled
# << files common

%files Xorg
%defattr(-,root,root,-)
# >> files Xorg
%{_bindir}/X
%{_bindir}/Xorg
%{_bindir}/gtf
%{_bindir}/cvt
%dir %{_libdir}/xorg
%dir %{_libdir}/xorg/modules
%dir %{_libdir}/xorg/modules/extensions
%{_libdir}/xorg/modules/extensions/libglx.so
%dir %{_libdir}/xorg/modules/multimedia
%{_libdir}/xorg/modules/multimedia/bt829_drv.so
%{_libdir}/xorg/modules/multimedia/fi1236_drv.so
%{_libdir}/xorg/modules/multimedia/msp3430_drv.so
%{_libdir}/xorg/modules/multimedia/tda8425_drv.so
%{_libdir}/xorg/modules/multimedia/tda9850_drv.so
%{_libdir}/xorg/modules/multimedia/tda9885_drv.so
%{_libdir}/xorg/modules/multimedia/uda1380_drv.so
%{_libdir}/xorg/modules/libexa.so
%{_libdir}/xorg/modules/libfb.so
%{_libdir}/xorg/modules/libint10.so
%{_libdir}/xorg/modules/libshadow.so
%{_libdir}/xorg/modules/libshadowfb.so
%{_libdir}/xorg/modules/libvbe.so
%{_libdir}/xorg/modules/libvgahw.so
%{_libdir}/xorg/modules/libfbdevhw.so
%{_libdir}/xorg/modules/libwfb.so
%doc %{_mandir}/man1/gtf.1*
%doc %{_mandir}/man1/Xorg.1*
%doc %{_mandir}/man1/cvt.1*
%doc %{_mandir}/man4/fbdevhw.4*
%doc %{_mandir}/man4/exa.4*
%doc %{_mandir}/man5/xorg.conf.5*
%doc %{_mandir}/man5/xorg.conf.d.5*
%dir %{_sysconfdir}/X11/xorg.conf.d
%dir %{_datadir}/X11/xorg.conf.d
%{_datadir}/X11/xorg.conf.d/10-evdev.conf
# << files Xorg

%files Xorg-setuid
%defattr(-,root,root,-)
# >> files Xorg-setuid
%{_bindir}/X
%attr(4711, root, root) %{_bindir}/Xorg
%{_bindir}/gtf
%{_bindir}/cvt
%dir %{_libdir}/xorg
%dir %{_libdir}/xorg/modules
%dir %{_libdir}/xorg/modules/extensions
%{_libdir}/xorg/modules/extensions/libglx.so
%dir %{_libdir}/xorg/modules/multimedia
%{_libdir}/xorg/modules/multimedia/bt829_drv.so
%{_libdir}/xorg/modules/multimedia/fi1236_drv.so
%{_libdir}/xorg/modules/multimedia/msp3430_drv.so
%{_libdir}/xorg/modules/multimedia/tda8425_drv.so
%{_libdir}/xorg/modules/multimedia/tda9850_drv.so
%{_libdir}/xorg/modules/multimedia/tda9885_drv.so
%{_libdir}/xorg/modules/multimedia/uda1380_drv.so
%{_libdir}/xorg/modules/libexa.so
%{_libdir}/xorg/modules/libfb.so
%{_libdir}/xorg/modules/libint10.so
%{_libdir}/xorg/modules/libshadow.so
%{_libdir}/xorg/modules/libshadowfb.so
%{_libdir}/xorg/modules/libvbe.so
%{_libdir}/xorg/modules/libvgahw.so
%{_libdir}/xorg/modules/libfbdevhw.so
%{_libdir}/xorg/modules/libwfb.so
%doc %{_mandir}/man1/gtf.1*
%doc %{_mandir}/man1/Xorg.1*
%doc %{_mandir}/man1/cvt.1*
%doc %{_mandir}/man4/fbdevhw.4*
%doc %{_mandir}/man4/exa.4*
%doc %{_mandir}/man5/xorg.conf.5*
%doc %{_mandir}/man5/xorg.conf.d.5*
%dir %{_sysconfdir}/X11/xorg.conf.d
%dir %{_datadir}/X11/xorg.conf.d
%{_datadir}/X11/xorg.conf.d/10-evdev.conf
# << files Xorg-setuid
