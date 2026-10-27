%global debug_package %{nil}
Name:       cache-api
Version:    1.0.0
Release:    1
Summary:    Flask caching proxy
License:    Proprietary
BuildArch:  noarch
Source0:    %{name}-%{version}.tar.gz
AutoReqProv: no

%description
Caching proxy (Flask + Redis) in front of Backend API.

%prep
%setup -q

%install
install -D -m 0755 cache-api.py      %{buildroot}/opt/cache-api/cache-api.py
install -D -m 0644 config.yaml       %{buildroot}/etc/cache-api/config.yaml
install -D -m 0644 cache-api.service %{buildroot}/lib/systemd/system/cache-api.service

%post
systemctl daemon-reload
systemctl enable --now cache-api.service

%preun
if [ $1 -eq 0 ]; then systemctl disable --now cache-api.service || true; fi

%files
/opt/cache-api/cache-api.py
%config(noreplace) /etc/cache-api/config.yaml
/lib/systemd/system/cache-api.service

%changelog
* Tue Oct 27 2026 Your Name <you@example.com> - 1.0.0-1
- Initial package
