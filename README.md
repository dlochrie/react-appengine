# Example App that uses a React app with an AppEngine backend.

## Both

From the root directory (might change):

  dev_appserver.py client/app.yaml app.yaml

NOTE: This assumes you build the client using `npm run build`.

## Server

From the root directory (might change):

    dev_appserver.py --host 0.0.0.0   --admin_host 127.0.0.1   --skip_sdk_update_check yes   . $*

## Client

In `./client`:

    npm start
