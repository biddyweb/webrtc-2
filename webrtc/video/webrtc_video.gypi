# Copyright (c) 2013 The WebRTC project authors. All Rights Reserved.
#
# Use of this source code is governed by a BSD-style license
# that can be found in the LICENSE file in the root of the source
# tree. An additional intellectual property rights grant can be found
# in the file PATENTS.  All contributing project authors may
# be found in the AUTHORS file in the root of the source tree.
{
  'variables': {
    'webrtc_video_dependencies': [
      '<(webrtc_root)/video_engine/video_engine.gyp:video_engine_core',
    ],
    'webrtc_video_sources': [
      'video/transport_adapter.cc',
      'video/transport_adapter.h',
      'video/video_receive_stream.cc',
      'video/video_receive_stream.h',
      'video/video_send_stream.cc',
      'video/video_send_stream.h',
    ],
  },
}
