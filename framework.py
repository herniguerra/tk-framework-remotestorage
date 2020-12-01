# Copyright (c) 2020 Shotgun Software Inc.
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights
# not expressly granted therein are reserved by Shotgun Software Inc.

"""
A framework that handles uploading and downloading of files from a cloud storage provider.
"""

import sgtk


class RemoteStorageFramework(sgtk.platform.Framework):
    def upload_publish(self, published_file):
        """
        Uploads a PublishedFile's path to the remote storage.
        :param published_file: dict
        :return: str path to uploaded file
        """
        paths = self.upload_publishes([published_file])[0]
        return paths[0] if len(paths) else None

    def upload_publishes(self, published_files):
        """
        Uploads a list of PublishedFile's paths to the remote storage.
        :param published_files: list of dicts
        :return: list of strings to the uploaded files
        """
        uploaded_files = []
        try:
            for published_file in published_files:
                self.engine.show_busy(
                    "Uploading", "Sending to mw_cloud: %s ..." % published_file["code"]
                )
                self.logger.debug(
                    "Executing upload hook for %s" % published_file)
                uploaded_files.append(
                    self.execute_hook_method(
                        "provider_hook", "upload", published_file=published_file
                    )
                )
        finally:
            self.engine.clear_busy()
        return uploaded_files

    def download_publish(self, published_file):
        """
        Downloads a list of PublishedFiles from the remote storage to the local storage.
        :param published_file: dict
        :return: str path to the downloaded file.
        """
        paths = self.download_publishes([published_file])
        return paths[0] if len(paths) else None

    def download_publishes(self, published_files):
        """
        Downloads a list of PublishedFiles from the remote storage to the local storage.
        :param published_files: list of dicts
        :return: list of strings of paths to the downloaded files.
        """
        downloaded_files = []
        try:
            for published_file in published_files:
                self.engine.show_busy(
                    "Download",
                    "Retrieving from mw_cloud: %s ..." % published_file["code"],
                )
                self.logger.debug(
                    "Executing download hook for %s" % published_file)
                downloaded_files.append(
                    self.execute_hook_method(
                        "provider_hook", "download", published_file=published_file
                    )
                )
        finally:
            self.engine.clear_busy()
        return downloaded_files

    def has_dependencies(self, published_file):
        import shotgun_api3

        sg = shotgun_api3.Shotgun(
            "https://many-worlds.shotgunstudio.com",
            script_name="mw_main_script",
            api_key="wmNnyhwfdpuecdstofw0^gjkk")

        published_file_id = published_file["id"]
        filters = [["id", "is", published_file_id]]
        fields = ["upstream_published_files"]
        publishedFile = sg.find_one("PublishedFile", filters, fields)

        print "HAS DEPENDENCIES??????????"
        print "?????????????????????????"
        print "?????????????????????????"
        print "?????????????????????????"
        print "?????????????????????????"
        print "?????????????????????????"
        print "?????????????????????????"
        print "?????????????????????????"
        print "?????????????????????????"
        print "?????????????????????????"
        print "?????????????????????????"
        print "?????????????????????????"
        print "?????????????????????????"
        print "?????????????????????????"
        print "?????????????????????????"
        print "?????????????????????????"

        if len(publishedFile["upstream_published_files"]) != 0:
            dependencies = []

            for dep in publishedFile["upstream_published_files"]:
                dependency_id = publishedFile["upstream_published_files"][0]["id"]
                filters = [["id", "is", dependency_id]]
                fields = ["path", "name", "published_file_type", "code"]
                dependency = sg.find_one("PublishedFile", filters, fields)
                dependencies.append(dependency)

            "***********************"
            "***********************"
            "***********************"
            "***********************"
            "***********************"
            "***********************"
            "***********************"
            "***********************"

            print dependencies
            return dependencies
        else:
            return None
