%define name grandr_applet
%define version 0.4.1
%define release %mkrel 1

Summary: Screen resolution changer applet for the GNOME panel
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://dekorte.homeip.net/download/grandr-applet/%{name}-%{version}.tar.gz
Patch: grandr_applet-0.3-deprecated.patch
URL: http://dekorte.homeip.net/download/grandr-applet/
License: GPL
Group: Graphical desktop/GNOME
BuildRoot: %{_tmppath}/%{name}-buildroot
Requires: gnome-panel
BuildRequires: libpanel-applet-devel

%description
GrandrApplet is a simple gnome-panel front end to the xrandr extension. You
can use it to switch the screen resolution and orientation on the fly.

%prep
%setup -q
%patch -p1
aclocal
autoconf
automake
#gw contains wrong path
rm -f GrandrApplet.server

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
rm -fr %buildroot/%_datadir/doc
%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-,root,root)
%doc ChangeLog NEWS README AUTHORS
%_libdir/bonobo/servers/GrandrApplet.server
%_libdir/grandr
%_datadir/pixmaps/grandr.png
