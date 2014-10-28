%if 0%{?fedora} > 12
%global with_python3 1
%else
%{!?__python2: %global __python2 /usr/bin/python2}
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print (get_python_lib())")}
%endif

%global srcname karaage-cluster-tools

Name: karaage-cluster-tools
Version: 0.0.2
Release: 1%{?dist}
Summary: Karaage cluster management tools

Group: Development/Libraries
License: GPL3+
Url: https://github.com/VPAC/pytsm/

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch
%if 0%{?with_python3}
BuildRequires:  python3-devel, python3-setuptools, python3-six, python3-flake8
%else
BuildRequires:  python2-devel, python-setuptools, python-six
%endif # if with_python2

%description
This package contains programs to be installed on a cluster for management of
the cluster.

At the present time it will automatically upload usage data to karaage for
processing with the karaage-usage plugin.

%prep

%build
%if 0%{?with_python3}
%{__python3} setup.py build
%else
%{__python2} setup.py build
%endif # with_python3

%install
rm -rf %{buildroot}

%if 0%{?with_python3}
%{__python3} setup.py install --skip-build --root $RPM_BUILD_ROOT
%else
%{__python2} setup.py install  --skip-build --root $RPM_BUILD_ROOT
%endif # with_python3

mkdir -p $RPM_BUILD_ROOT/etc/cron.d
cp debian/karaage-cluster-tools.cron.d $RPM_BUILD_ROOT/etc/cron.d/karaage-cluster-tools

%check

%if 0%{?with_python3}
%{__python2} /usr/bin/flake8 .
%{__python3} setup.py test
%else
#%{__python2} /usr/bin/flake8 .
%{__python2} setup.py test
%endif # with_python3

%clean
rm -rf $RPM_BUILD_ROOT

%files
%config(noreplace) /etc/cron.d/*
%config(noreplace) /etc/karaage3/*
/usr/bin/*
%if 0%{?with_python3}
%{python3_sitelib}/*
%else
%{python2_sitelib}/*
%endif # with_python3
