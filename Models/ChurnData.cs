using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace ChurnDashboard.Models
{
    // Informa ao Entity Framework qual tabela mapear no banco
    [Table("tb_churn_data")]
    public class ChurnData
    {
        [Key]
        public string? CustomerID { get; set; }
        public string? Gender { get; set; }
        public int SeniorCitizen { get; set; }
        public string? Partner { get; set; }
        public string? Dependents { get; set; }
        public int Tenure { get; set; }
        public string? PhoneService { get; set; }
        public string? MultipleLines { get; set; }
        public string? InternetService { get; set; }
        public string? OnlineSecurity { get; set; }
        public string? OnlineBackup { get; set; }
        public string? DeviceProtection { get; set; }
        public string? TechSupport { get; set; }
        public string? StreamingTV { get; set; }
        public string? StreamingMovies { get; set; }
        public string? Contract { get; set; }
        public string? PaperlessBilling { get; set; }
        public string? PaymentMethod { get; set; }
        public double MonthlyCharges { get; set; }
        public double TotalCharges { get; set; }
        public string? Churn { get; set; }
    }
}