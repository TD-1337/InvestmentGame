import pandas as pd

def export_to_csv(portfolio_dict):
    # Set var to check if dataframe needs to be created or appended
    create_df = 1

    # Get all orders and put them in a dataframe
    for y in portfolio_dict:
        if create_df == 1:
            # Create data frame with first portfolio
            export_df = pd.DataFrame([x.return_as_dict() for x in portfolio_dict[y].orders])
            # Turn off creation of data frame
            create_df = 0
        else:
            # Append to data frame
            export_df = export_df.append(pd.DataFrame([x.return_as_dict() for x in portfolio_dict[y].orders]))

    # Export the data frame to a csv
    export_df.to_csv('orders.csv', index=False)