# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps  # pylint: disable=unused-import


helps[
    "confcom"
] = """
    type: group
    short-summary: Commands to generate security policies for confidential containers in Azure.
"""

helps[
    "confcom acipolicygen"
] = """
    type: command
    short-summary: Create a Confidential Container Security Policy.

    parameters:
        - name: --input -i
          type: string
          short-summary: 'Input JSON config file'

        - name: --template-file -a
          type: string
          short-summary: 'Input ARM Template file'

        - name: --parameters -p
          type: string
          short-summary: 'Input parameters file to optionally accompany an ARM Template'

        - name: --image
          type: string
          short-summary: 'Input image name'

        - name: --tar
          type: string
          short-summary: 'Path to either a tarball containing image layers or a JSON file containing paths to tarballs of image layers'

        - name: --infrastructure-svn
          type: string
          short-summary: 'Minimum Allowed Software Version Number for Infrastructure Fragment'

        - name: --diff -d
          type: boolean
          short-summary: 'When combined with an input ARM Template, verifies the policy present in the ARM Template under "ccePolicy" and the containers within the ARM Template are compatible. If they are incompatible, a list of reasons is given and the exit status code will be 2.'

        - name: --json -j
          type: string
          short-summary: 'Outputs in JSON format instead of Rego'

        - name: --outraw
          type: boolean
          short-summary: 'Output policy in clear text compact JSON instead of default base64 format'

        - name: --outraw-pretty-print
          type: boolean
          short-summary: 'Output policy in clear text and pretty print format'

        - name: --save-to-file -s
          type: string
          short-summary: 'Save output policy to given file path.'

        - name: --print-policy
          type: boolean
          short-summary: 'When enabled, the generated security policy is printed to the command line instead of injected into the input ARM Template'

    examples:
        - name: Input a policy.json file to create a base64 encoded Confidential Container Security Policy
          text: az confcom acipolicygen --input "./policy.json"
        - name: Input a policy.json file to create a human-readable Confidential Container Security Policy
          text: az confcom acipolicygen --input "./policy.json" --outraw-pretty-print
        - name: Input a policy.json file to save a Confidential Container Security Policy to a file
          text: az confcom acipolicygen --input "./policy.json" -s "./output-file.txt"
"""
