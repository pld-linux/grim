Summary:	Grab images from a Wayland compositor
Name:		grim
Version:	1.4.0
Release:	1
License:	MIT
Group:		Applications
Source0:	https://github.com/emersion/grim/releases/download/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	003f029dd7b6ce5c994ed19ce46b82a3
URL:		https://wayland.emersion.fr/grim
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	meson >= 0.59.0
BuildRequires:	ninja
BuildRequires:	pixman-devel
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	scdoc
BuildRequires:	wayland-devel
BuildRequires:	wayland-protocols >= 1.14
Suggests:	slurp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Grab images from a Wayland compositor.

%prep
%setup -q

%build
%meson build
%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/grim
%{_mandir}/man1/grim.1*
