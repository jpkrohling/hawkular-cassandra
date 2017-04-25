Name:           hawkular-cassandra
Version:        3.0.12
Release:        1%{?dist}
Summary:        Apache Cassandra packaged by the Hawkular team

License:        Apache Software License 2.0
URL:            https://github.com/jpkrohling/cassandra-rpm
Source0:        https://github.com/apache/cassandra/archive/cassandra-3.0.12.tar.gz
Patch0:		      0001-Handle-exabyte-sized-filesystems.patch
BuildArch:      noarch

BuildRequires: ant >= 1.9
BuildRequires: ant-junit >= 1.9
BuildRequires: patch
BuildRequires: java-1.8.0-openjdk-devel

Requires:      jre >= 1.8.0
Requires:      python(abi) >= 2.7
Requires(pre): user(cassandra)
Requires(pre): group(cassandra)
Requires(pre): shadow-utils
Provides:      user(cassandra)
Provides:      group(cassandra)

%description

%prep
/usr/bin/gzip -dc %{_sourcedir}/cassandra-3.0.12.tar.gz | /usr/bin/tar -xof -

cd cassandra-cassandra-3.0.12
mkdir -p build/javadoc
%patch0 -p1
ant artifacts -Dversion=3.0.12 -Drelease=true

%install
export DONT_STRIP=1
cd %{buildroot}
mkdir opt
pushd opt
/usr/bin/gzip -dc %{_builddir}/cassandra-cassandra-3.0.12/build/apache-cassandra-3.0.12-bin.tar.gz | /usr/bin/tar -xof -
rm -rf %{buildroot}/opt/apache-cassandra-3.0.12/lib/sigar-bin
popd

%files
/opt

%changelog
* Thu Apr 20 2017 Juraci Paixão Kröhling <juraci@kroehling.de>
-
