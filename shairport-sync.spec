Name:           shairport-sync
Version:        3.1
Release:        1
Summary:        AirTunes emulator. Shairport Sync adds multi-room capability with Audio Synchronisation.

Group:          Applications/Multimedia
License:        GPL
URL:            https://github.com/mikebrady/shairport-sync
Source0:        https://github.com/mikebrady/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libconfig-devel
BuildRequires:  popt-devel
BuildRequires:  openssl-devel
BuildRequires:  libdaemon-devel
BuildRequires:  avahi-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  systemd-units
BuildRequires:  soxr-devel
Requires:       openssl
Requires:       avahi
Requires:       libdaemon
Requires:       alsa-lib
Requires:       soxr

%description
Shairport Sync emulates an AirPort Express for the purpose of streaming audio from iTunes, iPods, iPhones, iPads and AppleTVs. Audio played by a Shairport Sync-powered device stays synchronised with the source and hence with similar devices playing the same source. Thus, for example, synchronised multi-room audio is possible without difficulty. (Hence the name Shairport Sync, BTW.)

Shairport Sync does not support AirPlay video or photo streaming.

%prep
%setup -q

%build
autoreconf -i -f
%configure --with-avahi --with-alsa --with-ssl=openssl --with-soxr --with-systemd
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
rm %{buildroot}/etc/shairport-sync.conf.sample

%pre
getent group %{name} &>/dev/null || groupadd --system %{name} >/dev/null || true
getent passwd %{name} &> /dev/null || useradd --system -c "%{name} User" \
        -d %{_localstatedir}/%{name} -m -g %{name} -s /sbin/nologin \
        -G audio %{name} >/dev/null || true

%files
%config /etc/shairport-sync.conf
/usr/bin/shairport-sync
/usr/share/man/man7/shairport-sync.7.gz
%{_unitdir}/%{name}.service
%doc AUTHORS LICENSES README.md

%changelog
* Sun Aug 13 2017 Dmitry Fontanov <spukst3r@gmail.com>
- 

* Sun Aug 13 2017 Dmitry Fontanov <spukst3r@gmail.com>
- 3.1 (spukst3r@gmail.com)
- Automatic commit of package [shairport-sync] release [3.2-1].
  (spukst3r@gmail.com)
- Rollback tito's tag (spukst3r@gmail.com)
- Automatic commit of package [shairport-sync] release [3.2-1].
  (spukst3r@gmail.com)
- Failsafe user/group creation for makefile.am (spukst3r@gmail.com)

* Sun Aug 13 2017 Dmitry Fontanov <spukst3r@gmail.com> 3.2-1
- Rollback tito's tag (spukst3r@gmail.com)
- Automatic commit of package [shairport-sync] release [3.2-1].
  (spukst3r@gmail.com)
- Failsafe user/group creation for makefile.am (spukst3r@gmail.com)

* Sun Aug 13 2017 Dmitry Fontanov <spukst3r@gmail.com> 3.1-1
- Failsafe user/group creation for makefile.am (spukst3r@gmail.com)

* Sun Aug 13 2017 Dmitry Fontanov <spukst3r@gmail.com> 3.1-1
- ignore failed user creation (spukst3r@gmail.com)
- Version 3.1 (mikebrady@eircom.net)
- Version 3.1 (mikebrady@eircom.net)
- 3.1 (mikebrady@eircom.net)
- Update configure.ac (mikebrady@eircom.net)
- Better layout, thanks to https://github.com/vrs01 (mikebrady@eircom.net)
- Update README.md (mikebrady@eircom.net)
- Update configure.ac (mikebrady@eircom.net)
- Update README.md (mikebrady@eircom.net)
- Update README.md (mikebrady@eircom.net)
- Update README.md (mikebrady@eircom.net)
- Remove some (apparently) duplicate -O2 directives (mikebrady@eircom.net)
- Update UPDATING.md (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update FEDORA.md (mikebrady@eircom.net)
- Add info about the alsa mute_using_playback_switch setting
  (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Add info about the volume set hook (mikebrady@eircom.net)
- Update README.md (mikebrady@eircom.net)
- Update README.md (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Tidy up source using clang-format (mikebrady@eircom.net)
- small edits to the man files (mikebrady@eircom.net)
- make sndio formats case-insensitive, fix a little error message
  (mikebrady@eircom.net)
- Update manual and make the sndio format settings conform to the alsa settings
  (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Tidy up and/or suppress some debug messages (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Allow a zero silent lead-in time. (mikebrady@eircom.net)
- Quieten a debug message. (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Move common audio backend settings like buffer size and offsets to the
  "general" settings stanza. Improve the resync code a little.
  (mikebrady@eircom.net)
- Move common audio backend settings like buffer size and offsets to the
  "general" settings stanza. Improve the resync code a little.
  (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Add code to read audio_backend_silent_lead_in_time settings. Fix a few errors
  in the sample config file. (mikebrady@eircom.net)
- Add code to read audio_backend_silent_lead_in_time settings.
  (mikebrady@eircom.net)
- Correct examples of settings for buffer length and offset to include the
  suffix _in_seconds. Add the sample audio_backend_silent_lead_in_time
  settings. (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Quieten some debug messages. (mikebrady@eircom.net)
- Add some settings to the new PulseAudio backend. Limit the silent lead-in
  time on pipe and stdout backends. Not tested much. (mikebrady@eircom.net)
- Add some settings to the new PulseAudio backend. Limit the silent lead-in
  time to pipe and stdout backends. Not tested much. (mikebrady@eircom.net)
- read stdout from the on-start command to choose ALSA output device
  (cody@instructure.com)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Some calls to the "die" function need to be preceded by unlocking the alsa
  mutex. (mikebrady@eircom.net)
- Some calls to the "die" function need to be preceded by unlocking the alsa
  mutex. (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Fix silly bug whereby it was looking for the configuration file in the wrong
  place. (mikebrady@eircom.net)
- Fix silly bug whereby it was looking for the configuration file in the wrong
  place. (mikebrady@eircom.net)
- Fix typo in shairport-sync.c (troyliu0105@outlook.com)
- Stop generating multiple PA sound applications -- now, just generate one.
  (mikebrady@eircom.net)
- Fix pid_file_proc which was retuning a null (mikebrady@eircom.net)
- Try a different resync mechanism (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update configure.ac (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Add a brief comment about the chunking sub-protocol (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update shairport-sync.conf (mikebrady@eircom.net)
- Send metadata too large for UDP maximum message size into chunks.
  (paulguyot@ieee.org)
- Make sure socket send buffer is large enough for all metadata.
  (paulguyot@ieee.org)
- Update README.md (mikebrady@eircom.net)
- Update README.md (mikebrady@eircom.net)
- Update README.md (mikebrady@eircom.net)
- Update README.md (mikebrady@eircom.net)
- Update README.md (mikebrady@eircom.net)
- Incremental update (mikebrady@eircom.net)
- Update README.md (mikebrady@eircom.net)
- Update README.md (mikebrady@eircom.net)
- Update README.md (mikebrady@eircom.net)
- Add an extra option "-j" to daemonize withoput generating a PID file
  (mikebrady@eircom.net)
- Add an extra option "-j" to daemonize withoput generating a PID file
  (mikebrady@eircom.net)
- Change the order of evaluating command lione options so that the config file
  is read before any commands are executed. (mikebrady@eircom.net)
- Change the order of evaluating command lione options so that the config file
  is read before any commands are executed. (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Fix grammatical error in configure.ac (mikebrady@eircom.net)
- Update configure.ac (mikebrady@eircom.net)
- Add new bare-bones pulseaudio backend (mikebrady@eircom.net)
- Make default buffer 0.35 seconds, turn off some debug code.
  (mikebrady@eircom.net)
- Restore player.c modifications specific to pa -- not needed now.
  (mikebrady@eircom.net)
- Use lock and unlock to improve stability, ahem. (mikebrady@eircom.net)
- Cork output if underflow is detected. (mikebrady@eircom.net)
- Change service name to Shairport Sync (mikebrady@eircom.net)
- Initial very rough full-fat pulseaudio backend (mikebrady@eircom.net)
- Initial very rough full-fat pulseaudio backend (mikebrady@eircom.net)
- Update README.md (mikebrady@eircom.net)
- Update README.md (mikebrady@eircom.net)
- Update README.md (mikebrady@eircom.net)
- Update README.md (mikebrady@eircom.net)
- Update README.md (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Fix mixing of mono -- do 32-bit add and preserve all 17 bits for later
  dithering (mikebrady@eircom.net)
- Fix mixing of mono -- do 32-bit add and preserve all 17 bits for later
  dithering (mikebrady@eircom.net)
- Use hardware volume control only to mute when there is a mixer but no switch.
  (mikebrady@eircom.net)
- Use hardware volume control only to mute when there is a mixer but no switch.
  (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Improve the logic of the interplay between the volume and mute controls, so
  that if muted due to volume levels, will not be unmuted
  (mikebrady@eircom.net)
- Improve the logic of the interplay between the volume and mute controls, so
  that if muted due to volume levels, will not be unmuted
  (mikebrady@eircom.net)
- Signal presence or absence of hardware volume and mute abilities properly.
  Fix software-only mute. (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Don't turn the software volume down to zero when muting
  (mikebrady@eircom.net)
- Don't turn the software volume down to zero when muting
  (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Open and close the hardware mixer only when needed -- don't keep it open
  throughout the play session. This allows it to respond to external volume
  changes (mikebrady@eircom.net)
- Open and close the hardware mixer when needed -- don't keep it open
  throughout the play session. This allows it to respond to external volume
  changes (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Fix silly bug in volume adjust code (mikebrady@eircom.net)
- Fix silly bug in volume adjust code (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Add alsa_use_playback_switch_for_mute to the configuration data structure, so
  visible for debug summary. (mikebrady@eircom.net)
- Add ability do disable hardware mute (mikebrady@eircom.net)
- Only set volume if it has been asked for externally. Clean up mute. Add
  ability do disable hardware mute (mikebrady@eircom.net)
- Modify a debug message (mikebrady@eircom.net)
- Only set volume if it has been asked for externally. Clean up mute. Add
  ability do disable hardware mute (mikebrady@eircom.net)
- Only set volume if it has been asked for externally. Clean up mute. Add
  ability do disable hardware mute (mikebrady@eircom.net)
- Fixed desired buffer length for Pulseaudio (habbbe@gmail.com)
- Update README.md (mikebrady@eircom.net)
- Update shairport-sync.conf (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Add a "run_this_when_volume_is_set" facility to call a program when the
  volume is set. The AirPlay volume is passed. (mikebrady@eircom.net)
- Add a "run_this_when_volume_is_set" facility to call a program when the
  volume is set. The AirPlay volume is passed. (mikebrady@eircom.net)
- Update FREEBSD.md (mikebrady@eircom.net)
- Update FREEBSD.md (mikebrady@eircom.net)
- Update FREEBSD.md (mikebrady@eircom.net)
- Update FREEBSD.md (mikebrady@eircom.net)
- Update FREEBSD.md (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update System V and System D installers to define user, group and runtime
  directory as necessary (mikebrady@eircom.net)
- Improve startup script and make it optional (mikebrady@eircom.net)
- Add FreeBSD service and installation. Change default PID file directory.
  SystemV and SystemD scripts should be updated. (mikebrady@eircom.net)
- Update FREEBSD.md (mikebrady@eircom.net)
- Update FREEBSD.md (mikebrady@eircom.net)
- Update FREEBSD.md (mikebrady@eircom.net)
- Update FREEBSD.md (mikebrady@eircom.net)
- Update FREEBSD.md (mikebrady@eircom.net)
- Update FREEBSD.md (mikebrady@eircom.net)
- Update FREEBSD.md (mikebrady@eircom.net)
- Update configure.ac (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update FREEBSD.md (mikebrady@eircom.net)
- Improve the delay function by estimating the number of frames played during
  the interval (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Fix a few crashing bugs if there was no configuration file at all
  (mikebrady@eircom.net)
- Fix an inconsequential warning showing up in clang (mikebrady@eircom.net)
- Update LIBSOXR.md (mikebrady@eircom.net)
- Fix an error that prevented it from reporting delay correctly.
  (mikebrady@eircom.net)
- Improve debug messages a little (mikebrady@eircom.net)
- Update FREEBSD.md (mikebrady@eircom.net)
- Update FREEBSD.md (mikebrady@eircom.net)
- Update FREEBSD.md (mikebrady@eircom.net)
- Update FREEBSD.md (mikebrady@eircom.net)
- Update FREEBSD.md (mikebrady@eircom.net)
- Update configure.ac (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update shairport-sync.conf (mikebrady@eircom.net)
- Update FREEBSD.md (mikebrady@eircom.net)
- Fix off-by-one error in enumatering UDP ports in the port_range. Make the
  error message a little more useful. (mikebrady@eircom.net)
- Fix some warnings from clang on FreeBSD. One was significant -- the randarray
  stuff didn't look right. (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update FREEBSD.md (mikebrady@eircom.net)
- Update FREEBSD.md (mikebrady@eircom.net)
- Update README.md (mikebrady@eircom.net)
- Update README.md (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Create FREEBSD.md (mikebrady@eircom.net)
- FreeBSD doesn't have ETIME but both FreeBSD and Linux know ETIMEDOUT
  (git@tobik.me)
- Rewrite and unbreak sndio backend (git@tobik.me)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Bug fixes, improved error messaging, stability improvements, new
  --logOutputLevel option. (mikebrady@eircom.net)
- Add information about --logOutputLevel (mikebrady@eircom.net)
- Fix issue where sound from the last play was still there with the next play.
  Make timing stuff threadsaf, handle volume_max_db correctly when
  ignore_volume_control is true (mikebrady@eircom.net)
- Fix issue where sound from the last play was still there with the next play.
  Make timing stuff threadsafe (mikebrady@eircom.net)
- Add new command line option --logOutputLevel (mikebrady@eircom.net)
- Improve error reporting in non-blocking write code (mikebrady@eircom.net)
- Move some globals into the thread parameter block. Add setting for
  logOutputLevel (mikebrady@eircom.net)
- Move the code to cehck for ignoring volume control to player.c
  (mikebrady@eircom.net)
- Make this threadsafe and modify the clock drift diagnostics
  (mikebrady@eircom.net)
- Improve error reporting if stdout can't be  written to.
  (mikebrady@eircom.net)
- Improve error reporting if pipe can't be opened or written to.
  (mikebrady@eircom.net)
- Fully release the hardware device on flush. Simplify flushing. Also improve
  some debug messages. (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update configure.ac (mikebrady@eircom.net)
- Don't die if you can't change the volume control -- just report it
  (mikebrady@eircom.net)
- Fix various typos. (berkovskyy@gmail.com)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Make rtp stuff thread-safe -- remove all globals (mikebrady@eircom.net)
- Make rtp stuff thread-safe -- remove all globals (mikebrady@eircom.net)
- deglobalise sockets and reference timestamp (mikebrady@eircom.net)
- deglobalise self_scope_id for ipv6 (mikebrady@eircom.net)
- deglobalise client_ip_string and self_ip_string (mikebrady@eircom.net)
- Deglobalise rtp_running, make rtp timing sender use the conn data strucutre
  (mikebrady@eircom.net)
- Add rtp init and terminate, mirror all globals in the conn data structure
  (mikebrady@eircom.net)
- add conn to many procedure calls (mikebrady@eircom.net)
- Add some debug messages around requests to stop and wathc out for double
  announcements (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Fix audio backend latency offset calculations (mikebrady@eircom.net)
- Fix audio backend latency offset calculations (mikebrady@eircom.net)
- Add specific metadat message when a FLUSH message is received. Also add
  diabnostic for fmtp parameters. (mikebrady@eircom.net)
- Clean up creation of conversation thread -- no functional difference.
  (mikebrady@eircom.net)
- Update configure.ac (mikebrady@eircom.net)
- Add a memory barrier after initialising the rtsp_conn record. Stop a
  potential race condition. (mikebrady@eircom.net)
- Ignore .dirstamp files (mikebrady@eircom.net)
- Fix small bug in interpolation error message. (mikebrady@eircom.net)
- Stop the "ao", "pulse" and "sndio" backends from complaining about the new
  output rate and format information. (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Change the identified basck to ShairportSync -- lost in the move from 2.8.6
  to 3.0 (mikebrady@eircom.net)
- De-globalise ab_read and ab_write. player thread now fully reentrant.
  (mikebrady@eircom.net)
- Make the seq_diff... etc calls explicitly depend on a base value
  (mikebrady@eircom.net)
- De-globalise fix_volume and the vol_mutex (mikebrady@eircom.net)
- De globalise everything except ab_read and ab_write and the volume control
  stuff (mikebrady@eircom.net)
- Make initialising and destroying mutexes and condition variables internal to
  the player thread. (mikebrady@eircom.net)
- de-globalise flowcontrol ab_mutex,flush_mutex, first_packet_time_to_play,
  time_since_play_started (mikebrady@eircom.net)
- de-globalise missing_packets, late_packets, too_late_packets,
  resend_requests, decoder_in_use, last_seqno_read (mikebrady@eircom.net)
- De-globalise input_bytes_per_frame,output_bytes_per_frame,output_sample_ratio
  ,max_frame_size_change,decoder_info,shutdown_requested,connection_state_to_ou
  tput,player_thread_please_stop (mikebrady@eircom.net)
- De-globalise previous_random_number (mikebrady@eircom.net)
- De-globalise
  max_frames_per_packet,input_num_channels,input_bit_depth,input_rate
  (mikebrady@eircom.net)
- Change the order of initialisation back to waht it was before de-globalising
  the init_decoder, etc. (mikebrady@eircom.net)
- Move init and terminate decoder calls inside the player thread -- still using
  globals though (mikebrady@eircom.net)
- Move buffer inside player thread (mikebrady@eircom.net)
- Fix a bug to ensure a silent frame is supplied to replace a missing frame.
  (mikebrady@eircom.net)
- Untested, probably not working (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- change function die, warn, inform and debug change funcions die, warn, inform
  and debug argument from `char*` to `const char*` to prevent a warning in C==
  (yann.pomarede@gmail.com)
- adding -O2 (x2.6 speed up on Raspberry Pi) (yann.pomarede@gmail.com)
- FFTConvolver needs C++11 and -O2 divides by 3 CPU usage on a Raspberry Pi.
  (yann.pomarede@gmail.com)
- prevent loudness if hardware mixer is used (yann.pomarede@gmail.com)
- 2 audio filters added, a volume-dependent-loudness and a convolution filter.
  (yann.pomarede@gmail.com)
- Remove obselete stuffing code. (mikebrady@eircom.net)
- Add reference to `soundio` (mikebrady@eircom.net)
- Fix it up to 3.1d0 (mikebrady@eircom.net)
- Add back all accumulated changes to master branch at 3.0 release to 3.1d0
  (mikebrady@eircom.net)
- Add back all accumulated changes to master branch at 3.0 release
  (mikebrady@eircom.net)

* Sun Aug 13 2017 Dmitry Fontanov <spukst3r@gmail.com>
- ignore failed user creation (spukst3r@gmail.com)
- Version 3.1 (mikebrady@eircom.net)
- Version 3.1 (mikebrady@eircom.net)
- 3.1 (mikebrady@eircom.net)
- Update configure.ac (mikebrady@eircom.net)
- Better layout, thanks to https://github.com/vrs01 (mikebrady@eircom.net)
- Update README.md (mikebrady@eircom.net)
- Update configure.ac (mikebrady@eircom.net)
- Update README.md (mikebrady@eircom.net)
- Update README.md (mikebrady@eircom.net)
- Update README.md (mikebrady@eircom.net)
- Remove some (apparently) duplicate -O2 directives (mikebrady@eircom.net)
- Update UPDATING.md (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update FEDORA.md (mikebrady@eircom.net)
- Add info about the alsa mute_using_playback_switch setting
  (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Add info about the volume set hook (mikebrady@eircom.net)
- Update README.md (mikebrady@eircom.net)
- Update README.md (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Tidy up source using clang-format (mikebrady@eircom.net)
- small edits to the man files (mikebrady@eircom.net)
- make sndio formats case-insensitive, fix a little error message
  (mikebrady@eircom.net)
- Update manual and make the sndio format settings conform to the alsa settings
  (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Tidy up and/or suppress some debug messages (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Allow a zero silent lead-in time. (mikebrady@eircom.net)
- Quieten a debug message. (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Move common audio backend settings like buffer size and offsets to the
  "general" settings stanza. Improve the resync code a little.
  (mikebrady@eircom.net)
- Move common audio backend settings like buffer size and offsets to the
  "general" settings stanza. Improve the resync code a little.
  (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Add code to read audio_backend_silent_lead_in_time settings. Fix a few errors
  in the sample config file. (mikebrady@eircom.net)
- Add code to read audio_backend_silent_lead_in_time settings.
  (mikebrady@eircom.net)
- Correct examples of settings for buffer length and offset to include the
  suffix _in_seconds. Add the sample audio_backend_silent_lead_in_time
  settings. (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Quieten some debug messages. (mikebrady@eircom.net)
- Add some settings to the new PulseAudio backend. Limit the silent lead-in
  time on pipe and stdout backends. Not tested much. (mikebrady@eircom.net)
- Add some settings to the new PulseAudio backend. Limit the silent lead-in
  time to pipe and stdout backends. Not tested much. (mikebrady@eircom.net)
- read stdout from the on-start command to choose ALSA output device
  (cody@instructure.com)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Some calls to the "die" function need to be preceded by unlocking the alsa
  mutex. (mikebrady@eircom.net)
- Some calls to the "die" function need to be preceded by unlocking the alsa
  mutex. (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Fix silly bug whereby it was looking for the configuration file in the wrong
  place. (mikebrady@eircom.net)
- Fix silly bug whereby it was looking for the configuration file in the wrong
  place. (mikebrady@eircom.net)
- Fix typo in shairport-sync.c (troyliu0105@outlook.com)
- Stop generating multiple PA sound applications -- now, just generate one.
  (mikebrady@eircom.net)
- Fix pid_file_proc which was retuning a null (mikebrady@eircom.net)
- Try a different resync mechanism (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update configure.ac (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Add a brief comment about the chunking sub-protocol (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update shairport-sync.conf (mikebrady@eircom.net)
- Send metadata too large for UDP maximum message size into chunks.
  (paulguyot@ieee.org)
- Make sure socket send buffer is large enough for all metadata.
  (paulguyot@ieee.org)
- Update README.md (mikebrady@eircom.net)
- Update README.md (mikebrady@eircom.net)
- Update README.md (mikebrady@eircom.net)
- Update README.md (mikebrady@eircom.net)
- Update README.md (mikebrady@eircom.net)
- Incremental update (mikebrady@eircom.net)
- Update README.md (mikebrady@eircom.net)
- Update README.md (mikebrady@eircom.net)
- Update README.md (mikebrady@eircom.net)
- Add an extra option "-j" to daemonize withoput generating a PID file
  (mikebrady@eircom.net)
- Add an extra option "-j" to daemonize withoput generating a PID file
  (mikebrady@eircom.net)
- Change the order of evaluating command lione options so that the config file
  is read before any commands are executed. (mikebrady@eircom.net)
- Change the order of evaluating command lione options so that the config file
  is read before any commands are executed. (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Fix grammatical error in configure.ac (mikebrady@eircom.net)
- Update configure.ac (mikebrady@eircom.net)
- Add new bare-bones pulseaudio backend (mikebrady@eircom.net)
- Make default buffer 0.35 seconds, turn off some debug code.
  (mikebrady@eircom.net)
- Restore player.c modifications specific to pa -- not needed now.
  (mikebrady@eircom.net)
- Use lock and unlock to improve stability, ahem. (mikebrady@eircom.net)
- Cork output if underflow is detected. (mikebrady@eircom.net)
- Change service name to Shairport Sync (mikebrady@eircom.net)
- Initial very rough full-fat pulseaudio backend (mikebrady@eircom.net)
- Initial very rough full-fat pulseaudio backend (mikebrady@eircom.net)
- Update README.md (mikebrady@eircom.net)
- Update README.md (mikebrady@eircom.net)
- Update README.md (mikebrady@eircom.net)
- Update README.md (mikebrady@eircom.net)
- Update README.md (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Fix mixing of mono -- do 32-bit add and preserve all 17 bits for later
  dithering (mikebrady@eircom.net)
- Fix mixing of mono -- do 32-bit add and preserve all 17 bits for later
  dithering (mikebrady@eircom.net)
- Use hardware volume control only to mute when there is a mixer but no switch.
  (mikebrady@eircom.net)
- Use hardware volume control only to mute when there is a mixer but no switch.
  (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Improve the logic of the interplay between the volume and mute controls, so
  that if muted due to volume levels, will not be unmuted
  (mikebrady@eircom.net)
- Improve the logic of the interplay between the volume and mute controls, so
  that if muted due to volume levels, will not be unmuted
  (mikebrady@eircom.net)
- Signal presence or absence of hardware volume and mute abilities properly.
  Fix software-only mute. (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Don't turn the software volume down to zero when muting
  (mikebrady@eircom.net)
- Don't turn the software volume down to zero when muting
  (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Open and close the hardware mixer only when needed -- don't keep it open
  throughout the play session. This allows it to respond to external volume
  changes (mikebrady@eircom.net)
- Open and close the hardware mixer when needed -- don't keep it open
  throughout the play session. This allows it to respond to external volume
  changes (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Fix silly bug in volume adjust code (mikebrady@eircom.net)
- Fix silly bug in volume adjust code (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Add alsa_use_playback_switch_for_mute to the configuration data structure, so
  visible for debug summary. (mikebrady@eircom.net)
- Add ability do disable hardware mute (mikebrady@eircom.net)
- Only set volume if it has been asked for externally. Clean up mute. Add
  ability do disable hardware mute (mikebrady@eircom.net)
- Modify a debug message (mikebrady@eircom.net)
- Only set volume if it has been asked for externally. Clean up mute. Add
  ability do disable hardware mute (mikebrady@eircom.net)
- Only set volume if it has been asked for externally. Clean up mute. Add
  ability do disable hardware mute (mikebrady@eircom.net)
- Fixed desired buffer length for Pulseaudio (habbbe@gmail.com)
- Update README.md (mikebrady@eircom.net)
- Update shairport-sync.conf (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Add a "run_this_when_volume_is_set" facility to call a program when the
  volume is set. The AirPlay volume is passed. (mikebrady@eircom.net)
- Add a "run_this_when_volume_is_set" facility to call a program when the
  volume is set. The AirPlay volume is passed. (mikebrady@eircom.net)
- Update FREEBSD.md (mikebrady@eircom.net)
- Update FREEBSD.md (mikebrady@eircom.net)
- Update FREEBSD.md (mikebrady@eircom.net)
- Update FREEBSD.md (mikebrady@eircom.net)
- Update FREEBSD.md (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update System V and System D installers to define user, group and runtime
  directory as necessary (mikebrady@eircom.net)
- Improve startup script and make it optional (mikebrady@eircom.net)
- Add FreeBSD service and installation. Change default PID file directory.
  SystemV and SystemD scripts should be updated. (mikebrady@eircom.net)
- Update FREEBSD.md (mikebrady@eircom.net)
- Update FREEBSD.md (mikebrady@eircom.net)
- Update FREEBSD.md (mikebrady@eircom.net)
- Update FREEBSD.md (mikebrady@eircom.net)
- Update FREEBSD.md (mikebrady@eircom.net)
- Update FREEBSD.md (mikebrady@eircom.net)
- Update FREEBSD.md (mikebrady@eircom.net)
- Update configure.ac (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update FREEBSD.md (mikebrady@eircom.net)
- Improve the delay function by estimating the number of frames played during
  the interval (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Fix a few crashing bugs if there was no configuration file at all
  (mikebrady@eircom.net)
- Fix an inconsequential warning showing up in clang (mikebrady@eircom.net)
- Update LIBSOXR.md (mikebrady@eircom.net)
- Fix an error that prevented it from reporting delay correctly.
  (mikebrady@eircom.net)
- Improve debug messages a little (mikebrady@eircom.net)
- Update FREEBSD.md (mikebrady@eircom.net)
- Update FREEBSD.md (mikebrady@eircom.net)
- Update FREEBSD.md (mikebrady@eircom.net)
- Update FREEBSD.md (mikebrady@eircom.net)
- Update FREEBSD.md (mikebrady@eircom.net)
- Update configure.ac (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update shairport-sync.conf (mikebrady@eircom.net)
- Update FREEBSD.md (mikebrady@eircom.net)
- Fix off-by-one error in enumatering UDP ports in the port_range. Make the
  error message a little more useful. (mikebrady@eircom.net)
- Fix some warnings from clang on FreeBSD. One was significant -- the randarray
  stuff didn't look right. (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update FREEBSD.md (mikebrady@eircom.net)
- Update FREEBSD.md (mikebrady@eircom.net)
- Update README.md (mikebrady@eircom.net)
- Update README.md (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Create FREEBSD.md (mikebrady@eircom.net)
- FreeBSD doesn't have ETIME but both FreeBSD and Linux know ETIMEDOUT
  (git@tobik.me)
- Rewrite and unbreak sndio backend (git@tobik.me)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Bug fixes, improved error messaging, stability improvements, new
  --logOutputLevel option. (mikebrady@eircom.net)
- Add information about --logOutputLevel (mikebrady@eircom.net)
- Fix issue where sound from the last play was still there with the next play.
  Make timing stuff threadsaf, handle volume_max_db correctly when
  ignore_volume_control is true (mikebrady@eircom.net)
- Fix issue where sound from the last play was still there with the next play.
  Make timing stuff threadsafe (mikebrady@eircom.net)
- Add new command line option --logOutputLevel (mikebrady@eircom.net)
- Improve error reporting in non-blocking write code (mikebrady@eircom.net)
- Move some globals into the thread parameter block. Add setting for
  logOutputLevel (mikebrady@eircom.net)
- Move the code to cehck for ignoring volume control to player.c
  (mikebrady@eircom.net)
- Make this threadsafe and modify the clock drift diagnostics
  (mikebrady@eircom.net)
- Improve error reporting if stdout can't be  written to.
  (mikebrady@eircom.net)
- Improve error reporting if pipe can't be opened or written to.
  (mikebrady@eircom.net)
- Fully release the hardware device on flush. Simplify flushing. Also improve
  some debug messages. (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update configure.ac (mikebrady@eircom.net)
- Don't die if you can't change the volume control -- just report it
  (mikebrady@eircom.net)
- Fix various typos. (berkovskyy@gmail.com)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Make rtp stuff thread-safe -- remove all globals (mikebrady@eircom.net)
- Make rtp stuff thread-safe -- remove all globals (mikebrady@eircom.net)
- deglobalise sockets and reference timestamp (mikebrady@eircom.net)
- deglobalise self_scope_id for ipv6 (mikebrady@eircom.net)
- deglobalise client_ip_string and self_ip_string (mikebrady@eircom.net)
- Deglobalise rtp_running, make rtp timing sender use the conn data strucutre
  (mikebrady@eircom.net)
- Add rtp init and terminate, mirror all globals in the conn data structure
  (mikebrady@eircom.net)
- add conn to many procedure calls (mikebrady@eircom.net)
- Add some debug messages around requests to stop and wathc out for double
  announcements (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Fix audio backend latency offset calculations (mikebrady@eircom.net)
- Fix audio backend latency offset calculations (mikebrady@eircom.net)
- Add specific metadat message when a FLUSH message is received. Also add
  diabnostic for fmtp parameters. (mikebrady@eircom.net)
- Clean up creation of conversation thread -- no functional difference.
  (mikebrady@eircom.net)
- Update configure.ac (mikebrady@eircom.net)
- Add a memory barrier after initialising the rtsp_conn record. Stop a
  potential race condition. (mikebrady@eircom.net)
- Ignore .dirstamp files (mikebrady@eircom.net)
- Fix small bug in interpolation error message. (mikebrady@eircom.net)
- Stop the "ao", "pulse" and "sndio" backends from complaining about the new
  output rate and format information. (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Change the identified basck to ShairportSync -- lost in the move from 2.8.6
  to 3.0 (mikebrady@eircom.net)
- De-globalise ab_read and ab_write. player thread now fully reentrant.
  (mikebrady@eircom.net)
- Make the seq_diff... etc calls explicitly depend on a base value
  (mikebrady@eircom.net)
- De-globalise fix_volume and the vol_mutex (mikebrady@eircom.net)
- De globalise everything except ab_read and ab_write and the volume control
  stuff (mikebrady@eircom.net)
- Make initialising and destroying mutexes and condition variables internal to
  the player thread. (mikebrady@eircom.net)
- de-globalise flowcontrol ab_mutex,flush_mutex, first_packet_time_to_play,
  time_since_play_started (mikebrady@eircom.net)
- de-globalise missing_packets, late_packets, too_late_packets,
  resend_requests, decoder_in_use, last_seqno_read (mikebrady@eircom.net)
- De-globalise input_bytes_per_frame,output_bytes_per_frame,output_sample_ratio
  ,max_frame_size_change,decoder_info,shutdown_requested,connection_state_to_ou
  tput,player_thread_please_stop (mikebrady@eircom.net)
- De-globalise previous_random_number (mikebrady@eircom.net)
- De-globalise
  max_frames_per_packet,input_num_channels,input_bit_depth,input_rate
  (mikebrady@eircom.net)
- Change the order of initialisation back to waht it was before de-globalising
  the init_decoder, etc. (mikebrady@eircom.net)
- Move init and terminate decoder calls inside the player thread -- still using
  globals though (mikebrady@eircom.net)
- Move buffer inside player thread (mikebrady@eircom.net)
- Fix a bug to ensure a silent frame is supplied to replace a missing frame.
  (mikebrady@eircom.net)
- Untested, probably not working (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- change function die, warn, inform and debug change funcions die, warn, inform
  and debug argument from `char*` to `const char*` to prevent a warning in C==
  (yann.pomarede@gmail.com)
- adding -O2 (x2.6 speed up on Raspberry Pi) (yann.pomarede@gmail.com)
- FFTConvolver needs C++11 and -O2 divides by 3 CPU usage on a Raspberry Pi.
  (yann.pomarede@gmail.com)
- prevent loudness if hardware mixer is used (yann.pomarede@gmail.com)
- 2 audio filters added, a volume-dependent-loudness and a convolution filter.
  (yann.pomarede@gmail.com)
- Remove obselete stuffing code. (mikebrady@eircom.net)
- Add reference to `soundio` (mikebrady@eircom.net)
- Fix it up to 3.1d0 (mikebrady@eircom.net)
- Add back all accumulated changes to master branch at 3.0 release to 3.1d0
  (mikebrady@eircom.net)
- Add back all accumulated changes to master branch at 3.0 release
  (mikebrady@eircom.net)

* Sun Aug 13 2017 Dmitry Fontanov <spukst3r@gmail.com>
- ignore failed user creation (spukst3r@gmail.com)
- Version 3.1 (mikebrady@eircom.net)
- Version 3.1 (mikebrady@eircom.net)
- 3.1 (mikebrady@eircom.net)
- Update configure.ac (mikebrady@eircom.net)
- Better layout, thanks to https://github.com/vrs01 (mikebrady@eircom.net)
- Update README.md (mikebrady@eircom.net)
- Update configure.ac (mikebrady@eircom.net)
- Update README.md (mikebrady@eircom.net)
- Update README.md (mikebrady@eircom.net)
- Update README.md (mikebrady@eircom.net)
- Remove some (apparently) duplicate -O2 directives (mikebrady@eircom.net)
- Update UPDATING.md (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update FEDORA.md (mikebrady@eircom.net)
- Add info about the alsa mute_using_playback_switch setting
  (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Add info about the volume set hook (mikebrady@eircom.net)
- Update README.md (mikebrady@eircom.net)
- Update README.md (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Tidy up source using clang-format (mikebrady@eircom.net)
- small edits to the man files (mikebrady@eircom.net)
- make sndio formats case-insensitive, fix a little error message
  (mikebrady@eircom.net)
- Update manual and make the sndio format settings conform to the alsa settings
  (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Tidy up and/or suppress some debug messages (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Allow a zero silent lead-in time. (mikebrady@eircom.net)
- Quieten a debug message. (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Move common audio backend settings like buffer size and offsets to the
  "general" settings stanza. Improve the resync code a little.
  (mikebrady@eircom.net)
- Move common audio backend settings like buffer size and offsets to the
  "general" settings stanza. Improve the resync code a little.
  (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Add code to read audio_backend_silent_lead_in_time settings. Fix a few errors
  in the sample config file. (mikebrady@eircom.net)
- Add code to read audio_backend_silent_lead_in_time settings.
  (mikebrady@eircom.net)
- Correct examples of settings for buffer length and offset to include the
  suffix _in_seconds. Add the sample audio_backend_silent_lead_in_time
  settings. (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Quieten some debug messages. (mikebrady@eircom.net)
- Add some settings to the new PulseAudio backend. Limit the silent lead-in
  time on pipe and stdout backends. Not tested much. (mikebrady@eircom.net)
- Add some settings to the new PulseAudio backend. Limit the silent lead-in
  time to pipe and stdout backends. Not tested much. (mikebrady@eircom.net)
- read stdout from the on-start command to choose ALSA output device
  (cody@instructure.com)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Some calls to the "die" function need to be preceded by unlocking the alsa
  mutex. (mikebrady@eircom.net)
- Some calls to the "die" function need to be preceded by unlocking the alsa
  mutex. (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Fix silly bug whereby it was looking for the configuration file in the wrong
  place. (mikebrady@eircom.net)
- Fix silly bug whereby it was looking for the configuration file in the wrong
  place. (mikebrady@eircom.net)
- Fix typo in shairport-sync.c (troyliu0105@outlook.com)
- Stop generating multiple PA sound applications -- now, just generate one.
  (mikebrady@eircom.net)
- Fix pid_file_proc which was retuning a null (mikebrady@eircom.net)
- Try a different resync mechanism (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update configure.ac (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Add a brief comment about the chunking sub-protocol (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update shairport-sync.conf (mikebrady@eircom.net)
- Send metadata too large for UDP maximum message size into chunks.
  (paulguyot@ieee.org)
- Make sure socket send buffer is large enough for all metadata.
  (paulguyot@ieee.org)
- Update README.md (mikebrady@eircom.net)
- Update README.md (mikebrady@eircom.net)
- Update README.md (mikebrady@eircom.net)
- Update README.md (mikebrady@eircom.net)
- Update README.md (mikebrady@eircom.net)
- Incremental update (mikebrady@eircom.net)
- Update README.md (mikebrady@eircom.net)
- Update README.md (mikebrady@eircom.net)
- Update README.md (mikebrady@eircom.net)
- Add an extra option "-j" to daemonize withoput generating a PID file
  (mikebrady@eircom.net)
- Add an extra option "-j" to daemonize withoput generating a PID file
  (mikebrady@eircom.net)
- Change the order of evaluating command lione options so that the config file
  is read before any commands are executed. (mikebrady@eircom.net)
- Change the order of evaluating command lione options so that the config file
  is read before any commands are executed. (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Fix grammatical error in configure.ac (mikebrady@eircom.net)
- Update configure.ac (mikebrady@eircom.net)
- Add new bare-bones pulseaudio backend (mikebrady@eircom.net)
- Make default buffer 0.35 seconds, turn off some debug code.
  (mikebrady@eircom.net)
- Restore player.c modifications specific to pa -- not needed now.
  (mikebrady@eircom.net)
- Use lock and unlock to improve stability, ahem. (mikebrady@eircom.net)
- Cork output if underflow is detected. (mikebrady@eircom.net)
- Change service name to Shairport Sync (mikebrady@eircom.net)
- Initial very rough full-fat pulseaudio backend (mikebrady@eircom.net)
- Initial very rough full-fat pulseaudio backend (mikebrady@eircom.net)
- Update README.md (mikebrady@eircom.net)
- Update README.md (mikebrady@eircom.net)
- Update README.md (mikebrady@eircom.net)
- Update README.md (mikebrady@eircom.net)
- Update README.md (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Fix mixing of mono -- do 32-bit add and preserve all 17 bits for later
  dithering (mikebrady@eircom.net)
- Fix mixing of mono -- do 32-bit add and preserve all 17 bits for later
  dithering (mikebrady@eircom.net)
- Use hardware volume control only to mute when there is a mixer but no switch.
  (mikebrady@eircom.net)
- Use hardware volume control only to mute when there is a mixer but no switch.
  (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Improve the logic of the interplay between the volume and mute controls, so
  that if muted due to volume levels, will not be unmuted
  (mikebrady@eircom.net)
- Improve the logic of the interplay between the volume and mute controls, so
  that if muted due to volume levels, will not be unmuted
  (mikebrady@eircom.net)
- Signal presence or absence of hardware volume and mute abilities properly.
  Fix software-only mute. (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Don't turn the software volume down to zero when muting
  (mikebrady@eircom.net)
- Don't turn the software volume down to zero when muting
  (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Open and close the hardware mixer only when needed -- don't keep it open
  throughout the play session. This allows it to respond to external volume
  changes (mikebrady@eircom.net)
- Open and close the hardware mixer when needed -- don't keep it open
  throughout the play session. This allows it to respond to external volume
  changes (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Fix silly bug in volume adjust code (mikebrady@eircom.net)
- Fix silly bug in volume adjust code (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Add alsa_use_playback_switch_for_mute to the configuration data structure, so
  visible for debug summary. (mikebrady@eircom.net)
- Add ability do disable hardware mute (mikebrady@eircom.net)
- Only set volume if it has been asked for externally. Clean up mute. Add
  ability do disable hardware mute (mikebrady@eircom.net)
- Modify a debug message (mikebrady@eircom.net)
- Only set volume if it has been asked for externally. Clean up mute. Add
  ability do disable hardware mute (mikebrady@eircom.net)
- Only set volume if it has been asked for externally. Clean up mute. Add
  ability do disable hardware mute (mikebrady@eircom.net)
- Fixed desired buffer length for Pulseaudio (habbbe@gmail.com)
- Update README.md (mikebrady@eircom.net)
- Update shairport-sync.conf (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Add a "run_this_when_volume_is_set" facility to call a program when the
  volume is set. The AirPlay volume is passed. (mikebrady@eircom.net)
- Add a "run_this_when_volume_is_set" facility to call a program when the
  volume is set. The AirPlay volume is passed. (mikebrady@eircom.net)
- Update FREEBSD.md (mikebrady@eircom.net)
- Update FREEBSD.md (mikebrady@eircom.net)
- Update FREEBSD.md (mikebrady@eircom.net)
- Update FREEBSD.md (mikebrady@eircom.net)
- Update FREEBSD.md (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update System V and System D installers to define user, group and runtime
  directory as necessary (mikebrady@eircom.net)
- Improve startup script and make it optional (mikebrady@eircom.net)
- Add FreeBSD service and installation. Change default PID file directory.
  SystemV and SystemD scripts should be updated. (mikebrady@eircom.net)
- Update FREEBSD.md (mikebrady@eircom.net)
- Update FREEBSD.md (mikebrady@eircom.net)
- Update FREEBSD.md (mikebrady@eircom.net)
- Update FREEBSD.md (mikebrady@eircom.net)
- Update FREEBSD.md (mikebrady@eircom.net)
- Update FREEBSD.md (mikebrady@eircom.net)
- Update FREEBSD.md (mikebrady@eircom.net)
- Update configure.ac (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update FREEBSD.md (mikebrady@eircom.net)
- Improve the delay function by estimating the number of frames played during
  the interval (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Fix a few crashing bugs if there was no configuration file at all
  (mikebrady@eircom.net)
- Fix an inconsequential warning showing up in clang (mikebrady@eircom.net)
- Update LIBSOXR.md (mikebrady@eircom.net)
- Fix an error that prevented it from reporting delay correctly.
  (mikebrady@eircom.net)
- Improve debug messages a little (mikebrady@eircom.net)
- Update FREEBSD.md (mikebrady@eircom.net)
- Update FREEBSD.md (mikebrady@eircom.net)
- Update FREEBSD.md (mikebrady@eircom.net)
- Update FREEBSD.md (mikebrady@eircom.net)
- Update FREEBSD.md (mikebrady@eircom.net)
- Update configure.ac (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update shairport-sync.conf (mikebrady@eircom.net)
- Update FREEBSD.md (mikebrady@eircom.net)
- Fix off-by-one error in enumatering UDP ports in the port_range. Make the
  error message a little more useful. (mikebrady@eircom.net)
- Fix some warnings from clang on FreeBSD. One was significant -- the randarray
  stuff didn't look right. (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update FREEBSD.md (mikebrady@eircom.net)
- Update FREEBSD.md (mikebrady@eircom.net)
- Update README.md (mikebrady@eircom.net)
- Update README.md (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Create FREEBSD.md (mikebrady@eircom.net)
- FreeBSD doesn't have ETIME but both FreeBSD and Linux know ETIMEDOUT
  (git@tobik.me)
- Rewrite and unbreak sndio backend (git@tobik.me)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Bug fixes, improved error messaging, stability improvements, new
  --logOutputLevel option. (mikebrady@eircom.net)
- Add information about --logOutputLevel (mikebrady@eircom.net)
- Fix issue where sound from the last play was still there with the next play.
  Make timing stuff threadsaf, handle volume_max_db correctly when
  ignore_volume_control is true (mikebrady@eircom.net)
- Fix issue where sound from the last play was still there with the next play.
  Make timing stuff threadsafe (mikebrady@eircom.net)
- Add new command line option --logOutputLevel (mikebrady@eircom.net)
- Improve error reporting in non-blocking write code (mikebrady@eircom.net)
- Move some globals into the thread parameter block. Add setting for
  logOutputLevel (mikebrady@eircom.net)
- Move the code to cehck for ignoring volume control to player.c
  (mikebrady@eircom.net)
- Make this threadsafe and modify the clock drift diagnostics
  (mikebrady@eircom.net)
- Improve error reporting if stdout can't be  written to.
  (mikebrady@eircom.net)
- Improve error reporting if pipe can't be opened or written to.
  (mikebrady@eircom.net)
- Fully release the hardware device on flush. Simplify flushing. Also improve
  some debug messages. (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update configure.ac (mikebrady@eircom.net)
- Don't die if you can't change the volume control -- just report it
  (mikebrady@eircom.net)
- Fix various typos. (berkovskyy@gmail.com)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Make rtp stuff thread-safe -- remove all globals (mikebrady@eircom.net)
- Make rtp stuff thread-safe -- remove all globals (mikebrady@eircom.net)
- deglobalise sockets and reference timestamp (mikebrady@eircom.net)
- deglobalise self_scope_id for ipv6 (mikebrady@eircom.net)
- deglobalise client_ip_string and self_ip_string (mikebrady@eircom.net)
- Deglobalise rtp_running, make rtp timing sender use the conn data strucutre
  (mikebrady@eircom.net)
- Add rtp init and terminate, mirror all globals in the conn data structure
  (mikebrady@eircom.net)
- add conn to many procedure calls (mikebrady@eircom.net)
- Add some debug messages around requests to stop and wathc out for double
  announcements (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Fix audio backend latency offset calculations (mikebrady@eircom.net)
- Fix audio backend latency offset calculations (mikebrady@eircom.net)
- Add specific metadat message when a FLUSH message is received. Also add
  diabnostic for fmtp parameters. (mikebrady@eircom.net)
- Clean up creation of conversation thread -- no functional difference.
  (mikebrady@eircom.net)
- Update configure.ac (mikebrady@eircom.net)
- Add a memory barrier after initialising the rtsp_conn record. Stop a
  potential race condition. (mikebrady@eircom.net)
- Ignore .dirstamp files (mikebrady@eircom.net)
- Fix small bug in interpolation error message. (mikebrady@eircom.net)
- Stop the "ao", "pulse" and "sndio" backends from complaining about the new
  output rate and format information. (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- Change the identified basck to ShairportSync -- lost in the move from 2.8.6
  to 3.0 (mikebrady@eircom.net)
- De-globalise ab_read and ab_write. player thread now fully reentrant.
  (mikebrady@eircom.net)
- Make the seq_diff... etc calls explicitly depend on a base value
  (mikebrady@eircom.net)
- De-globalise fix_volume and the vol_mutex (mikebrady@eircom.net)
- De globalise everything except ab_read and ab_write and the volume control
  stuff (mikebrady@eircom.net)
- Make initialising and destroying mutexes and condition variables internal to
  the player thread. (mikebrady@eircom.net)
- de-globalise flowcontrol ab_mutex,flush_mutex, first_packet_time_to_play,
  time_since_play_started (mikebrady@eircom.net)
- de-globalise missing_packets, late_packets, too_late_packets,
  resend_requests, decoder_in_use, last_seqno_read (mikebrady@eircom.net)
- De-globalise input_bytes_per_frame,output_bytes_per_frame,output_sample_ratio
  ,max_frame_size_change,decoder_info,shutdown_requested,connection_state_to_ou
  tput,player_thread_please_stop (mikebrady@eircom.net)
- De-globalise previous_random_number (mikebrady@eircom.net)
- De-globalise
  max_frames_per_packet,input_num_channels,input_bit_depth,input_rate
  (mikebrady@eircom.net)
- Change the order of initialisation back to waht it was before de-globalising
  the init_decoder, etc. (mikebrady@eircom.net)
- Move init and terminate decoder calls inside the player thread -- still using
  globals though (mikebrady@eircom.net)
- Move buffer inside player thread (mikebrady@eircom.net)
- Fix a bug to ensure a silent frame is supplied to replace a missing frame.
  (mikebrady@eircom.net)
- Untested, probably not working (mikebrady@eircom.net)
- Update RELEASENOTES.md (mikebrady@eircom.net)
- change function die, warn, inform and debug change funcions die, warn, inform
  and debug argument from `char*` to `const char*` to prevent a warning in C==
  (yann.pomarede@gmail.com)
- adding -O2 (x2.6 speed up on Raspberry Pi) (yann.pomarede@gmail.com)
- FFTConvolver needs C++11 and -O2 divides by 3 CPU usage on a Raspberry Pi.
  (yann.pomarede@gmail.com)
- prevent loudness if hardware mixer is used (yann.pomarede@gmail.com)
- 2 audio filters added, a volume-dependent-loudness and a convolution filter.
  (yann.pomarede@gmail.com)
- Remove obselete stuffing code. (mikebrady@eircom.net)
- Add reference to `soundio` (mikebrady@eircom.net)
- Fix it up to 3.1d0 (mikebrady@eircom.net)
- Add back all accumulated changes to master branch at 3.0 release to 3.1d0
  (mikebrady@eircom.net)
- Add back all accumulated changes to master branch at 3.0 release
  (mikebrady@eircom.net)

* Tue Jun 13 2017 Dmitry Fontanov <spukst3r@gmail.com> 3.0-2
- Bumped spec release (spukst3r@gmail.com)
- Dropped libpopt from requires (spukst3r@gmail.com)

* Tue Jun 13 2017 Dmitry Fontanov <spukst3r@gmail.com>
- Bumped spec release (spukst3r@gmail.com)
- Dropped libpopt from requires (spukst3r@gmail.com)

* Tue Jun 13 2017 Unknown name 3.0-1
- new package built with tito

* Fri Feb 24 2017 Mike Brady <mikebrady@eircom.net> 2.8.6
- Many changes including 8- 16- 24- and 32-bit output
* Fri Oct 21 2016 Mike Brady <mikebrady@eircom.net> 2.8.6
- Advertise self as ShairportSync rather than AirPort device 2.8.6
* Sun Sep 25 2016 Mike Brady <mikebrady@eircom.net> 2.8.5
- Bug fixes and small enhancements 2.8.5
* Sat May 28 2016 Mike Brady <mikebrady@eircom.net> 2.8.4
- Bug fixes and a few small enhancements 2.8.4
* Fri Apr 15 2016 Mike Brady <mikebrady@eircom.net> 2.8.2
- Stability improvements, bug fixes and a few special-purpose settings 2.8.2
* Wed Mar 02 2016 Mike Brady <mikebrady@eircom.net> 2.8.1
- Stability improvements and important bug fixes 2.8.1
* Sat Jan 30 2016 Mike Brady <mikebrady@eircom.net> 2.8.0
- Enhancements and bug fixes 2.8.0
* Sun Oct 18 2015 Mike Brady <mikebrady@eircom.net> 2.6
- Important enhancements and bug fixes 2.6
* Thu Aug 27 2015 Mike Brady <mikebrady@eircom.net> 2.4.1
- Minor bug fixes 2.4.1
* Thu Aug 27 2015 Mike Brady <mikebrady@eircom.net> 2.4
- Prepare for stable release 2.4
* Wed Aug 26 2015 Mike Brady <mikebrady@eircom.net> 2.3.13.1-1
- Harmonise release numbers
* Fri Jul 24 2015 Bill Peck <bill@pecknet.com> 2.3.7-1
- Initial spec file
