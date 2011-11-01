Name:           instantbird
Version:        1.1
Release:        1%{?dist}
Summary:        Simple and powerful IM-client

License:        MPL
URL:            http://instantbird.com
Source0:        http://instantbird.com/downloads/%{version}/%{name}-%{version}.src.tgz

#BuildRequires:  build-essential
BuildRequires:  autoconf213
BuildRequires:  python
BuildRequires:  yasm
BuildRequires:  gtk2-devel
BuildRequires:  libxml2-devel
BuildRequires:  libIDL-devel
BuildRequires:  libXt-devel
BuildRequires:  libcurl-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  libnotify-devel
BuildRequires:  wireless-tools-devel
BuildRequires:  mesa-libGL-devel
#Requires:       

%description
Powerful and simple IM-client

%prep
%setup -q -n %{name}-%{version}-src


%build
make -f client.mk build


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%files
%doc



%changelog
* Tue Nov 01 2011 Vasiliy N. Glazov <vascom2@gmail.com> - 1.1-1.R
- Initial release