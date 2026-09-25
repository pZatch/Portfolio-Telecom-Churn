using Microsoft.AspNetCore.Mvc;
using ChurnDashboard.Data;
using System.Linq;

namespace ChurnDashboard.Controllers
{
    public class HomeController : Controller
    {
        private readonly AppDbContext _context;

        public HomeController(AppDbContext context)
        {
            _context = context;
        }

        public IActionResult Index()
        {
            // 1. KPIs Executivos
            var totalCustomers = _context.ChurnDataSet.Count();
            var totalChurn = _context.ChurnDataSet.Count(c => c.Churn == "Yes");
            var churnRate = totalCustomers > 0 ? (double)totalChurn / totalCustomers * 100 : 0;
            var mrrLost = _context.ChurnDataSet.Where(c => c.Churn == "Yes").Sum(c => c.MonthlyCharges);

            ViewBag.TotalCustomers = totalCustomers;
            ViewBag.TotalChurn = totalChurn;
            ViewBag.ChurnRate = churnRate;
            ViewBag.MrrLost = mrrLost;

            // 2. Análise de Ofensores: Churn por Tipo de Contrato
            var churnByContract = _context.ChurnDataSet
                .Where(c => c.Churn == "Yes")
                .GroupBy(c => c.Contract)
                .Select(g => new { Contract = g.Key, Count = g.Count() })
                .ToList();

            ViewBag.ContractLabels = churnByContract.Select(c => c.Contract).ToArray();
            ViewBag.ContractData = churnByContract.Select(c => c.Count).ToArray();

            // 3. Análise de Ofensores: Churn por Internet Service
            var churnByInternet = _context.ChurnDataSet
                .Where(c => c.Churn == "Yes")
                .GroupBy(c => c.InternetService)
                .Select(g => new { Service = g.Key, Count = g.Count() })
                .ToList();

            ViewBag.InternetLabels = churnByInternet.Select(c => c.Service).ToArray();
            ViewBag.InternetData = churnByInternet.Select(c => c.Count).ToArray();

            return View();
        }
    }
}