Name: xplsprinters
Version: 1.0.1
Release: %mkrel 4
Summary: Shows a list of Xprint printers and it's attributes
Group: Development/X11
Source: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxp-devel >= 1.0.0
BuildRequires: libxprintutil-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1

%description
Xplsprinters is a utility for Xprint, the printing system for the X Window
system.  It can deliver both a list of printers and attributes supported for a
specific list of printers.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

#

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/xplsprinters
%{_mandir}/man1/xplsprinters.1x*


