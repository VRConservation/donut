import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# Read the CSV files
sierra = pd.read_csv('sierra.csv')
shasta = pd.read_csv('shasta.csv')

# Function to clean and convert data
def clean_data(df):
    df['Crown Fire Probability'] = pd.to_numeric(df['Crown Fire Probability'])
    df['Sum of acres treated'] = df['Sum of acres treated'].astype(str).str.replace(',', '')
    df['Sum of acres treated'] = pd.to_numeric(df['Sum of acres treated'])
    return df

sierra = clean_data(sierra)
shasta = clean_data(shasta)

# Function to bin data into thirds and calculate percentages
def bin_data(df):
    # Define bins: low, medium, high based on thirds of actual probability range
    min_prob = df['Crown Fire Probability'].min()
    max_prob = df['Crown Fire Probability'].max()
    third = (max_prob - min_prob) / 3
    
    bins = [min_prob - 1, min_prob + third, min_prob + 2*third, max_prob + 1]
    labels = ['Low', 'Medium', 'High']
    
    df_copy = df.copy()
    df_copy['Bin'] = pd.cut(df_copy['Crown Fire Probability'], bins=bins, labels=labels)
    
    # Sum acres by bin
    binned = df_copy.groupby('Bin', observed=True)['Sum of acres treated'].sum()
    
    # Calculate percentages
    total = binned.sum()
    percentages = (binned / total) * 100
    return percentages

sierra_binned = bin_data(sierra)
shasta_binned = bin_data(shasta)

# Function to create chart
def create_chart(data, filename, label):
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Set dark background
    fig.patch.set_facecolor('#2b2b2b')
    ax.set_facecolor('#2b2b2b')
    
    # Define colors for bins
    bin_colors = {'Low': '#2ecc71', 'Medium': '#f1c40f', 'High': '#e74c3c'}
    colors = [bin_colors[bin_label] for bin_label in data.index]
    
    # Create bar chart
    bars = ax.bar(range(len(data)), data.values, color=colors, width=0.6)
    
    # Set x-axis labels
    ax.set_xticks(range(len(data)))
    ax.set_xticklabels(data.index)
    
    # Style the axes
    ax.spines['bottom'].set_color('white')
    ax.spines['left'].set_color('white')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    # Style ticks and labels
    ax.tick_params(colors='white')
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    
    # Add grid lines (horizontal)
    ax.grid(axis='y', color='white', linestyle='-', linewidth=0.7, alpha=0.3)
    ax.set_axisbelow(True)
    
    # Set labels
    ax.set_xlabel('Crown Fire Probability', fontsize=12, color='white')
    ax.set_ylabel('Percentage of acres treated (%)', fontsize=12, color='white')
    
    # Format y-axis as percentages
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x:.1f}%'))
    
    # Save figure
    plt.tight_layout()
    plt.savefig(filename, facecolor='#2b2b2b', edgecolor='none', dpi=150)
    plt.close()
    
    print(f"Created {filename}")

# Create charts
create_chart(sierra_binned, 'sierra_binned.png', 'Sierra')
create_chart(shasta_binned, 'shasta_binned.png', 'Shasta')

# Print summary
print("\nSierra binned data:")
print(sierra_binned)
print("\nShasta binned data:")
print(shasta_binned)
