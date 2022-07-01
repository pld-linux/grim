Summary:	Grab images from a Wayland compositor
Name:		grim
Version:	1.4.0
Release:	3
License:	MIT
Group:		Applications
Source0:	https://github.com/emersion/grim/releases/download/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	003f029dd7b6ce5c994ed19ce46b82a3
Patch0:		printf_format.patch
URL:		https://wayland.emersion.fr/grim
BuildRequires:	bash-completion-devel
BuildRequires:	fish-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	meson >= 0.59.0
BuildRequires:	ninja
BuildRequires:	pixman-devel
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	scdoc
BuildRequires:	wayland-devel
BuildRequires:	wayland-protocols >= 1.14
Suggests:	slurp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Grab images from a Wayland compositor.

%package -n bash-completion-grim
Summary:	bash-completion for grim
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	bash-completion >= 2.0
BuildArch:	noarch

%description -n bash-completion-grim
This package provides bash-completion for grim.

%package -n fish-completion-grim
Summary:	Fish completion for grim command
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	fish
BuildArch:	noarch

%description -n fish-completion-grim
Fish completion for grim command.

%prep
%setup -q
%patch0 -p1

%build
%meson build \
	-Dfish-completions=true \
	-Dbash-completions=true
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

%files -n bash-completion-grim
%defattr(644,root,root,755)
%{bash_compdir}/grim.bash

%files -n fish-completion-%{name}
%defattr(644,root,root,755)
%{fish_compdir}/grim.fish
