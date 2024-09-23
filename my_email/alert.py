from argparse import ArgumentParser
from mailer import send_email


def setup_args(parser):
    """Setup the arguments for the script.

    This function configures the command-line arguments that the script accepts.
    The script allows users to send an email by specifying the sender, recipient,
    subject, and body through command-line arguments.

    Args:
        parser (ArgumentParser): An ArgumentParser object that is used to define
        and parse the command-line arguments.

    Returns:
        ArgumentParser: The ArgumentParser object with the arguments for the script added.

    Example:
        To use the script, you would run it from the command line like this:

        >>> python alert.py -s sender@example.com -r recipient@example.com -j "Test Alert" -b "This is a test email."

        This would send an email from 'sender@example.com' to 'recipient@example.com'
        with the subject "Test Alert" and the body "This is a test email."

    Arguments:
        -s/--sender: The email address of the sender. (Required)
        -r/--recipient: The email address of the recipient. (Required)
        -j/--subject: The subject of the email. (Optional, default is "Subject")
        -b/--body: The body of the email. (Optional, default is "Body")
    """
    parser.add_argument("-s", "--sender", type=str, required=True)
    parser.add_argument("-r", "--recipient", type=str, required=True)
    parser.add_argument("-j", "--subject", type=str, default="Subject")
    parser.add_argument("-b", "--body", type=str, default="Body")
    return parser


def main():
    """Main function to parse arguments and send an email.

    This function parses the command-line arguments, then calls the `send_email`
    function with the provided sender, recipient, subject, and body.

    The script is designed to be run from the command line and will use the
    `ArgumentParser` to process user input for email details.

    Example:
        To run this script, you can execute the following command:

        >>> python alert.py -s sender@example.com -r recipient@example.com -j "Test Subject" -b "This is a test email."

        This will send an email based on the provided inputs.
    """
    parser = ArgumentParser()
    args = setup_args(parser).parse_args()

    send_email(
        sender=args.sender,
        recipient=args.recipient,
        subject=args.subject,
        body=args.body,
    )


if __name__ == "__main__":
    main()
