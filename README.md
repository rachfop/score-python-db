# Score Hello World

A simple Score project deploying a Python database application.

## Deploying

[Score](https://score.dev/) is used to deploy the workload to Humanitec.

You can see an example command for this inside [`deploy.sh`](./deploy.sh).

## The Workload

The workload is a Python application with Flask and a MySQL database.

## The Application

1. **Build the Docker image**:

To build the Docker image, run:

```bash
./build-image.sh
```

2. **Deploy using Humanitec**:

To deploy the workload to Humanitec, use the [`deploy.sh`](./deploy.sh) script.
Which uses the [Score CLI](https://score.dev/docs/cli) to deploy the workload to Humanitec.

```bash
./deploy.sh
```

This will build the Docker image and push it to the Humanitec registry.
You need to set the following environment variables:

   - `HUMANITEC_APP_ID` - The ID of the app in Humanitec
   - `HUMANITEC_ORG` - The ID of the org in Humanitec
   - `HUMANITEC_TOKEN` - The token to authenticate with Humanitec


3. **(optional) Run locally**:

If you want to run the Docker container locally without deploying to Humanitec, you can do so with:

To build and run:

Build the Docker image:

```bash
docker build -t my-python-app:latest .
```

Run locally:

```bash
docker run -p 8080:8080 my-python-app:latest
```

## Troubleshooting

The error message "Unknown database 'score'" indicates that the MySQL server you're connecting to does not have a database named `score`.

Here's what you can do to address this:

**Create the Database**:

If the database doesn't exist, you'll need to create it. Connect to your MySQL server on your host machine and create the database:

```bash
mysql -u root -p -h 127.0.0.1
```

Once you're in the MySQL shell, run:

```sql
CREATE DATABASE score;
```

Then exit the MySQL shell:

```sql
exit;
```

**Check Database Name**:

Ensure that the database name in your Python application's configuration (`db_config`) matches the actual name of the database in your MySQL server. If you intended to use a different database name, update the `db_config` accordingly.

**Database User Permissions**:

Ensure that the MySQL user specified in your `db_config` has the necessary permissions to access the `score` database. You can grant permissions using:

```sql
GRANT ALL PRIVILEGES ON score.* TO 'username'@'host.docker.internal' IDENTIFIED BY 'password';
FLUSH PRIVILEGES;
```

Replace `username` and `password` with the appropriate values from your `db_config`.

**Re-run the Docker Container**:

After making the necessary changes, try running your Docker container again:

```bash
docker run -p 8080:8080 my-python-app:latest
```

By ensuring the database exists and that your application's configuration matches the actual setup of your MySQL server, you should be able to resolve the "Unknown database" error.


**`error exec format error`**:

The `error exec format error`  typically indicates a mismatch between the architecture of the binary you're trying to execute and the architecture of the system you're running it on.

This is a known error when building Docker images on Apple Silicon (M1) Macs.

Because of this include the `--platform linux/amd64` flag when building the Docker image.
If the error persists, include `export DOCKER_DEFAULT_PLATFORM=linux/amd64` on your host machine when building the Docker image.