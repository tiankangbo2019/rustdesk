Name:       redesk
Version:    1.4.6
Release:    0
Summary:    RPM package
License:    GPL-3.0
URL:        https://rustdesk.com
Vendor:     redesk <info@rustdesk.com>
Requires:   gtk3 libxcb libXfixes alsa-lib libva pam gstreamer1-plugins-base
Recommends: libayatana-appindicator-gtk3 libxdo
Provides:   libdesktop_drop_plugin.so()(64bit), libdesktop_multi_window_plugin.so()(64bit), libfile_selector_linux_plugin.so()(64bit), libflutter_custom_cursor_plugin.so()(64bit), libflutter_linux_gtk.so()(64bit), libscreen_retriever_plugin.so()(64bit), libtray_manager_plugin.so()(64bit), liburl_launcher_linux_plugin.so()(64bit), libwindow_manager_plugin.so()(64bit), libwindow_size_plugin.so()(64bit), libtexture_rgba_renderer_plugin.so()(64bit)

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Scriptlets/

%description
The best open-source remote desktop client software, written in Rust.

%prep
# we have no source, so nothing here

%build
# we have no source, so nothing here

# %global __python %{__python3}

%install

mkdir -p "%{buildroot}/usr/share/redesk" && cp -r ${HBB}/flutter/build/linux/x64/release/bundle/* -t "%{buildroot}/usr/share/redesk"
mkdir -p "%{buildroot}/usr/bin"
install -Dm 644 $HBB/res/redesk.service -t "%{buildroot}/usr/share/redesk/files"
install -Dm 644 $HBB/res/redesk.desktop -t "%{buildroot}/usr/share/redesk/files"
install -Dm 644 $HBB/res/redesk-link.desktop -t "%{buildroot}/usr/share/redesk/files"
install -Dm 644 $HBB/res/128x128@2x.png "%{buildroot}/usr/share/icons/hicolor/256x256/apps/redesk.png"
install -Dm 644 $HBB/res/scalable.svg "%{buildroot}/usr/share/icons/hicolor/scalable/apps/redesk.svg"

%files
/usr/share/redesk/*
/usr/share/redesk/files/redesk.service
/usr/share/icons/hicolor/256x256/apps/redesk.png
/usr/share/icons/hicolor/scalable/apps/redesk.svg
/usr/share/redesk/files/redesk.desktop
/usr/share/redesk/files/redesk-link.desktop

%changelog
# let's skip this for now

%pre
# can do something for centos7
case "$1" in
  1)
    # for install
  ;;
  2)
    # for upgrade
    systemctl stop redesk || true
  ;;
esac

%post
cp /usr/share/redesk/files/redesk.service /etc/systemd/system/redesk.service
cp /usr/share/redesk/files/redesk.desktop /usr/share/applications/
cp /usr/share/redesk/files/redesk-link.desktop /usr/share/applications/
ln -sf /usr/share/redesk/redesk /usr/bin/redesk
systemctl daemon-reload
systemctl enable redesk
systemctl start redesk
update-desktop-database

%preun
case "$1" in
  0)
    # for uninstall
    systemctl stop redesk || true
    systemctl disable redesk || true
    rm /etc/systemd/system/redesk.service || true
  ;;
  1)
    # for upgrade
  ;;
esac

%postun
case "$1" in
  0)
    # for uninstall
    rm /usr/bin/redesk || true
    rmdir /usr/lib/redesk || true
    rmdir /usr/local/redesk || true
    rmdir /usr/share/redesk || true
    rm /usr/share/applications/redesk.desktop || true
    rm /usr/share/applications/redesk-link.desktop || true
    update-desktop-database
  ;;
  1)
    # for upgrade
    rmdir /usr/lib/redesk || true
    rmdir /usr/local/redesk || true
  ;;
esac
