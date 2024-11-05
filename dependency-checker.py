import importlib
import pkg_resources

def check_dependencies():
    # List of required packages and their purposes
    dependencies = {
        'tensorflow': 'Deep learning framework',
        'pandas': 'Data manipulation and analysis',
        'numpy': 'Numerical computing',
        'nltk': 'Natural Language Processing toolkit',
        'scikit-learn': 'Machine learning utilities',
        'keras': 'Deep learning library (part of TensorFlow)'
    }
    
    print("Checking dependencies...\n")
    missing_packages = []
    installed_versions = {}
    
    for package, purpose in dependencies.items():
        try:
            # Get installed version
            version = pkg_resources.get_distribution(package).version
            installed_versions[package] = version
        except pkg_resources.DistributionNotFound:
            missing_packages.append(package)
    
    # Print results
    print("Found packages:")
    print("-" * 50)
    for package, version in installed_versions.items():
        print(f"{package:<15} v{version:<10} - {dependencies[package]}")
    
    if missing_packages:
        print("\nMissing packages:")
        print("-" * 50)
        for package in missing_packages:
            print(f"{package:<15} - {dependencies[package]}")
        print("\nInstall missing packages using:")
        print(f"pip install {' '.join(missing_packages)}")
    else:
        print("\nAll required packages are installed!")
    
    # Additional NLTK data check
    print("\nChecking NLTK data...")
    try:
        import nltk
        nltk.data.find('corpora/stopwords')
        print("NLTK stopwords are installed")
    except LookupError:
        print("NLTK stopwords are not installed. Install using:")
        print("nltk.download('stopwords')")
    
    # Check for GPU support in TensorFlow
    print("\nChecking TensorFlow GPU support...")
    try:
        import tensorflow as tf
        if tf.test.is_built_with_cuda():
            print("TensorFlow is built with CUDA")
            print(f"Available GPUs: {tf.config.list_physical_devices('GPU')}")
        else:
            print("TensorFlow is not built with CUDA (CPU-only)")
    except Exception as e:
        print(f"Error checking TensorFlow GPU support: {e}")

if __name__ == "__main__":
    check_dependencies()
